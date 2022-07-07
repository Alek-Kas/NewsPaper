from django_filters import FilterSet
from .models import Post


class PostFilter(FilterSet):
    class Meta:
        model = Post
        # В fields мы описываем по каким полям модели
        # будет производиться фильтрация.
        fields = {
            'post_heading': ['icontains'],
            'post_cat': ['icontains'],
            'post_time': ['gt'],  # позже указываемой даты
        }
