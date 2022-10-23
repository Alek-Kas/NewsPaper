from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.template.loader import render_to_string

from .models import PostCategory
from .tasks import mail_after_create


def send_notifications(text, pk, title, subscribers):
    html_content = render_to_string(
        'post_created_email.html',
        {
            'text': f'{text[:50]}',
            'link': f'{settings.SITE_URL}/news/{pk}',
        }
    )
    msg = EmailMultiAlternatives(
        subject=title,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        bcc=subscribers,
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()


@receiver(m2m_changed, sender=PostCategory)
def notify_about_new_post(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        categories = instance.post_cat.all()
        subscribers: list[str] = []
        for category in categories:
            subscribers += category.subscribers.all()
            print(subscribers)

        subscribers = [s.email for s in subscribers]
        print(subscribers)

        # send_notifications(instance.post_text, instance.pk, instance.post_heading, subscribers)
        mail_after_create(instance.post_text, instance.pk, instance.post_heading, subscribers)
