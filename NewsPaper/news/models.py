from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Author(models.Model):  # наследуемся от класса Model
    rating = models.IntegerField(default=0)
    staff = models.OneToOneField(User, on_delete=models.CASCADE())


# weather = 'WE'
# sports = 'SP'
# politics = 'PO'
# education = 'ED'
# incidents = 'IN'
# economy = 'EC'


class Category(models.Model):
    # CAT = [
    #     (weather, 'Погода'),
    #     (sports, 'Спорт'),
    #     (politics, 'Политика'),
    #     (education, 'Образование'),
    #     (incidents, 'Проишествия'),
    #     (economy, 'Экономика')
    # ]
    cat = models.CharField(max_length=64,
                           # choices=CAT,
                           # default=weather,
                           unique=True)

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
    post_time = models.DateTimeField()
    post_heading = models.CharField(max_length=64)
    post_text = models.CharField(max_length=1024)
    post_rating = models.IntegerField(default=0)
    post_author = models.ForeignKey(Author, on_delete=models.CASCADE())
    post_cat = models.ManyToManyField(PostCategory)


class PostCategory(models.Model):
    post_cat_post = models.ManyToManyField(Post)
    post_cat_cat = models.ManyToManyField(Category)


class Comment(models.Model):
    comment_text = models.CharField(max_length=128)
    comment_time = models.DateTimeField()
    comment_rating = models.IntegerField(default=0)
    comment_post = models.ForeignKey(Post)
    comment_user = models.ForeignKey(User)
