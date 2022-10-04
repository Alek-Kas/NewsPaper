# from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse
from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from .filters import PostFilter
from .forms import PostForm, AuthorForm, CategoryForm
from .models import Post, Author, Category, SubscribersUsers


# from django.db.models.signals import post_save
# from django.dispatch import receiver

# @receiver(post_save, sender=Post)
# def notify_post_new(sender, instance, create, **kwargs):
#     mail_subsriber(
#         subject=f'{instance.Post.post_heading}',
#         message=instance.message
#     )
#     print(f'{instance.Post.post_heading} {instance.message}')


# post_save.connect(notify_post_new, sender=Post)


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

    # pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #print(context)
        for category in self.get_object().post_cat.all():
            context['is_subscriber'] = self.request.user.category_set.filter(pk=category.pk).exists()
        print(context)
        print(context['is_subscriber'])
        return context


@login_required
def add_subscribe(request, **kwargs):
    cat_number = int(kwargs['pk'])
    print(cat_number)
    Category.objects.get(pk=cat_number).subscribers.add(request.user)
    return redirect('/news/')


@login_required
def delete_subscribe(request, **kwargs):
    cat_number = int(kwargs['pk'])
    print(cat_number)
    Category.objects.get(pk=cat_number).subscribers.remove(request.user)
    return redirect('/news/')

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


class NewsCreate(PermissionRequiredMixin, CreateView):
    form_class = PostForm
    model = Post
    permission_required = ('news.add_post',)
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


class ArticlesCreate(PermissionRequiredMixin, CreateView):
    form_class = PostForm
    model = Post
    permission_required = ('news.add_post',)
    template_name = 'articles/articles_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.post_type = 'article'
        post.post_author = Author.objects.get(author_user=self.request.user)
        return super().form_valid(form)


class PostDelete(PermissionRequiredMixin, DeleteView):
    model = Post
    # print(model, model.post_heading, model.pk)
    template_name = 'news/news_delete.html'
    permission_required = ('news.delete_post',)
    success_url = reverse_lazy('newslist')


class PostUpdate(PermissionRequiredMixin, UpdateView):
    form_class = PostForm
    model = Post
    permission_required = ('news.change_post',)
    template_name = 'news/news_edit.html'


class AuthorUpdate(LoginRequiredMixin, UpdateView):
    form_class = AuthorForm
    model = Author
    template_name = 'news/author_edit.html'


class SubscribeCreate(LoginRequiredMixin, CreateView):
    # model = Category
    model = SubscribersUsers
    # ordering = 'cat'
    form_class = CategoryForm
    template_name = 'news/subscribe.html'
    # print(str(Category.pk))


class SubscribeUpdate(LoginRequiredMixin, UpdateView):
    # model = Category
    model = SubscribersUsers
    # ordering = 'cat'
    form_class = CategoryForm
    template_name = 'news/subscribe.html'
    # print(str(Category.pk))
