# from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView

from .filters import PostFilter
from .forms import PostForm
from .models import Post


class NewsList(ListView):
    model = Post
    ordering = '-post_time'
    template_name = 'news/news_list.html'
    context_object_name = 'newslist'
    paginate_by = 10


class NewsDetail(DetailView):
    model = Post
    # Используем другой шаблон — news.html
    template_name = 'news/news.html'
    context_object_name = 'news'


class NewsSearch(ListView):
    model = Post
    ordering = '-post_time'
    template_name = 'news/search.html'
    context_object_name = 'newssearch'
    paginate_by = 10

    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        # Используем наш класс фильтрации.
        # self.request.GET содержит объект QueryDict, который мы рассматривали
        # в этом юните ранее.
        # Сохраняем нашу фильтрацию в объекте класса,
        # чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = PostFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset
        return context


class NewsCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'news/news_create.html'
