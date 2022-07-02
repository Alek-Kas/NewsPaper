# from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from .models import Post


class NewsList(ListView):
    model = Post
    ordering = '-post_time'
    template_name = 'news/news_list.html'
    context_object_name = 'newslist'


class NewsDetail(DetailView):
    model = Post
    # Используем другой шаблон — news.html
    template_name = 'news/news.html'
    context_object_name = 'news'
