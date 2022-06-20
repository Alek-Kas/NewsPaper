from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Author(models.Model):  # наследуемся от класса Model
    rating = models.IntegerField(default=0)
    staff = models.OneToOneField(User, on_delete=models.CASCADE)

    #  Метод update_rating() модели Author, который обновляет рейтинг пользователя, переданный в аргумент этого метода
    def update_rating(self):
        pass


class Category(models.Model):
    cat = models.CharField(max_length=64, unique=True)


article = 'AR'
news = 'NE'


class Post(models.Model):
    POST = [
        (article, 'Статья'),
        (news, 'Новость')
    ]
    post = models.CharField(max_length=2,
                            choices=POST,
                            default=article)
    post_time = models.DateTimeField(auto_now_add=True)
    post_heading = models.CharField(max_length=64)
    post_text = models.TextField(max_length=1024)
    post_rating = models.IntegerField(default=0)
    post_author = models.ForeignKey('Author', on_delete=models.CASCADE)
    post_cat = models.ManyToManyField('Category', through='PostCategory')

    #  Методы like() и dislike() в моделях Comment и Post, которые увеличивают/уменьшают рейтинг на единицу
    def like(self):
        pass

    def dislike(self):
        pass

    #  Метод preview() модели Post, который возвращает начало статьи (предварительный просмотр)
    #  длиной 124 символа и добавляет многоточие в конце.
    def preview(self):
        pass


class PostCategory(models.Model):
    post_cat_post = models.ForeignKey('Post', on_delete=models.CASCADE)
    post_cat_cat = models.ForeignKey('Category', on_delete=models.CASCADE)


class Comment(models.Model):
    comment_text = models.CharField(max_length=128)
    comment_time = models.DateTimeField(auto_now_add=True)
    comment_rating = models.IntegerField(default=0)
    comment_post = models.ForeignKey('Post', on_delete=models.CASCADE)
    comment_user = models.ForeignKey('User', on_delete=models.CASCADE)

    #  Методы like() и dislike() в моделях Comment и Post, которые увеличивают/уменьшают рейтинг на единицу
    #  суммарный рейтинг каждой статьи автора умножается на 3;
    #  суммарный рейтинг всех комментариев автора;
    #  суммарный рейтинг всех комментариев к статьям автора.
    def like(self):
        pass

    def dislike(self):
        pass
