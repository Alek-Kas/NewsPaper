from django_filters import FilterSet
from .models import Post


class PostFilter(FilterSet):
    class Meta:
        model = Post
        # В fields мы описываем по каким полям модели
        # будет производиться фильтрация.
        fields = {
            'post_heading': ['icontains'],
            'post_cat': ['exact'],
            #  'post_time': ['year__gt'],  # позже указываемой даты
        }
        # filter_overrides = {
        #     model.
        # }
