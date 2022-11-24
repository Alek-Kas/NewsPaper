from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum
from django.utils.translation import gettext as _
from django.utils.translation import pgettext_lazy

from django.urls import reverse
from django.core.cache import cache


class Author(models.Model):  # наследуемся от класса Model
    rating = models.IntegerField(default=0, verbose_name=pgettext_lazy('Rating', 'Rating'))
    author_user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=pgettext_lazy('Author', 'Author'))

    #  Метод update_rating() модели Author, который обновляет рейтинг пользователя, переданный в аргумент этого метода
    #  суммарный рейтинг каждой статьи автора умножается на 3;
    #  суммарный рейтинг всех комментариев автора;
    #  суммарный рейтинг всех комментариев к статьям автора.
    def update_rating(self):
        post_rat = self.post_set.aggregate(post_rating=Sum('post_rating'))
        pr = 0
        pr += post_rat.get('post_rating')

        com_rat = self.author_user.comment_set.aggregate(com_rating=Sum('comment_rating'))
        cr = 0
        cr += com_rat.get('com_rating')

        self.rating = pr * 3 + cr
        self.save()

    def __str__(self):
        return f'{self.author_user}'

    def get_absolute_url(self):
        return reverse('authorupdate', args=[str(self.id)])

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Category(models.Model):
    cat = models.CharField(
        max_length=64,
        unique=True,
        # help_text='Категория поста',
        help_text=_('Категория поста'),
        verbose_name=pgettext_lazy('Category', 'Category'))
    subscribers = models.ManyToManyField(
        User, through='SubscribersUsers', verbose_name=pgettext_lazy('Subscribers', 'Subscribers')
    )

    def __str__(self):
        return f'{self.cat}'

    def get_absolute_url(self):
        return reverse('subscribeupdate', args=[str(self.id)])

    class Meta:
        verbose_name = pgettext_lazy('Category', 'Category')
        verbose_name_plural = pgettext_lazy('Categories', 'Categories')


article = 'AR'
news = 'NE'


class Post(models.Model):
    POST = (
        (article, 'Статья'),
        (news, 'Новость')
    )
    post_type = models.CharField(max_length=2,
                                 choices=POST,
                                 default=article,
                                 verbose_name=pgettext_lazy('Post type', 'Post type'))
    post_time = models.DateTimeField(auto_now_add=True)
    post_heading = models.CharField(max_length=64, verbose_name=pgettext_lazy('Post heading', 'Post title'))
    post_text = models.TextField(max_length=1024, verbose_name=pgettext_lazy('Text of the post', 'Text of the post'))
    post_rating = models.IntegerField(default=0, verbose_name=pgettext_lazy('Post rating', 'Post rating'))
    post_author = models.ForeignKey(
        Author, on_delete=models.CASCADE, verbose_name=pgettext_lazy('Author of the post', 'Author of the post')
    )
    post_cat = models.ManyToManyField(
        Category, through='PostCategory', verbose_name=pgettext_lazy('Post category', 'Post category')
    )

    #  Методы like() и dislike() в моделях Comment и Post, которые увеличивают/уменьшают рейтинг на единицу
    def like(self):
        self.post_rating += 1
        self.save()

    def dislike(self):
        self.post_rating -= 1
        self.save()

    #  Метод preview() модели Post, который возвращает начало статьи (предварительный просмотр)
    #  длиной 124 символа и добавляет многоточие в конце.
    def preview(self):
        return f'{self.post_text[0:123]} ...'

    def __str__(self):
        return f'"{self.post_heading}" написал {self.post_author}'

    def get_absolute_url(self):
        return reverse('news', args=[str(self.id)])

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # сначала вызываем метод родителя, чтобы объект сохранился
        cache.delete(f'post-{self.pk}')  # затем удаляем его из кэша, чтобы сбросить его

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['post_time']  # Порядок/сортировка вывода (по умолчанию по pk)


class PostCategory(models.Model):
    post_cat_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    post_cat_cat = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    comment_text = models.CharField(max_length=128)
    comment_time = models.DateTimeField(auto_now_add=True)
    comment_rating = models.IntegerField(default=0)
    comment_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE)

    #  Методы like() и dislike() в моделях Comment и Post, которые увеличивают/уменьшают рейтинг на единицу
    def like(self):
        self.comment_rating += 1
        self.save()

    def dislike(self):
        self.comment_rating -= 1
        self.save()


class SubscribersUsers(models.Model):
    sub_cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('newslist')
