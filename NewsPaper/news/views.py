from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import ListView

from .models import Post


class NewsList(ListView):
    model = Post
    ordering = 'id'
    template_name = 'NewsPaper/news_list.html'
    context_object_name = 'newslist'
    # template_name = 'news.html'
    # def newslist(request):
    #     print('Кто-то зашёл на главную!')
    #     return HttpResponse('Привет!')
