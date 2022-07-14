# from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse
from datetime import datetime

from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from .filters import PostFilter
from .forms import PostForm
from .models import Post, Author


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

    def form_valid(self, form):
        post = form.save(commit=False)
        # f = self
        # print('То что в self ', self)
        # print('То что в form ', form)
        post.post_type = 'news'
        # post.post_time = datetime.utcnow()
        # post.post_author_id = 1
        post.post_author = Author.objects.get(author_user=self.request.user)
        return super().form_valid(form)


class ArticlesCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'articles/articles_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.post_type = 'article'
        post.post_author = Author.objects.get(author_user=self.request.user)
        return super().form_valid(form)


class PostDelete(DeleteView):
    model = Post
    # print(model, model.post_heading, model.pk)
    template_name = 'news/news_delete.html'
    success_url = reverse_lazy('newslist')


class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'news/news_edit.html'
