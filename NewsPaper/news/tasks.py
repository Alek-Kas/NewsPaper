import datetime

from celery import shared_task
import time

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from .models import Post, Category


@shared_task
def t_p():
    print('Print from news.tasks every minute')


@shared_task
def mailing_m_8am():
    today = datetime.datetime.now()
    last_week = today - datetime.timedelta(days=7)
    posts = Post.objects.filter(post_time__gte=last_week)
    print('Posts: ', posts)
    categories_test = set(posts.values_list('post_cat__cat', flat=True))
    categories = set()
    for s in categories_test:
        print(s)
        if s is not None:
            categories.add(s)
    print('categories: ', categories)
    subscribers_test = set(Category.objects.filter(cat__in=categories).values_list('subscribers__email', flat=True))
    print('subscribers: ', subscribers_test)
    subscribers = set()
    for s in subscribers_test:
        print(s)
        if s is not None:
            subscribers.add(s)
    print('subscribers без None: ', subscribers)
    html_content = render_to_string(
        'daily_post.html',
        {
            'link': settings.SITE_URL,
            'posts': posts,
        }
    )
    msg = EmailMultiAlternatives(
        subject='Статьи за неделю',
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )
    msg.attach_alternative(html_content, 'text/html')
    print('Message: ', msg)
    msg.send()
