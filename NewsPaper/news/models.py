from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum


# Create your models here.


class Author(models.Model):  # наследуемся от класса Model
    # full_name = models.CharField()
    rating = models.IntegerField(default=0)
    author_user = models.OneToOneField(User, on_delete=models.CASCADE)

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


class Category(models.Model):
    cat = models.CharField(max_length=64, unique=True)


article = 'AR'
news = 'NE'


class Post(models.Model):
    POST = (
        (article, 'Статья'),
        (news, 'Новость')
    )
    post_type = models.CharField(max_length=2,
                                 choices=POST,
                                 default=article)
    post_time = models.DateTimeField(auto_now_add=True)
    post_heading = models.CharField(max_length=64)
    post_text = models.TextField(max_length=1024)
    post_rating = models.IntegerField(default=0)
    post_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post_cat = models.ManyToManyField(Category, through='PostCategory')

    #  Методы like() и dislike() в моделях Comment и Post, которые увеличивают/уменьшают рейтинг на единицу
    def like(self):
        self.post_rating += 1
        self.save()
        # rating = self.post_rating
        # return self.post_rating += 1

    def dislike(self):
        self.post_rating -= 1
        self.save()
        # rating = self.post_rating
        # return self.post_rating -= 1

    #  Метод preview() модели Post, который возвращает начало статьи (предварительный просмотр)
    #  длиной 124 символа и добавляет многоточие в конце.
    def preview(self):
        return f'{self.post_text[0:123]} ...'


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
        # rating = self.comment_rating
        # return self.comment_rating += 1

    def dislike(self):
        self.comment_rating -= 1
        self.save()
        # rating = self.comment_rating
        # return self.comment_rating -= 1
