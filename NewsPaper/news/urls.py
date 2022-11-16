from django.urls import path
from .views import (
    NewsList,
    NewsDetail,
    NewsSearch,
    NewsCreate,
    PostDelete,
    PostUpdate,
    ArticlesCreate,
    AuthorUpdate,
    SubscribeUpdate, SubscribeCreate, add_subscribe, delete_subscribe,
)
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', cache_page(60*5)(NewsList.as_view()), name='newslist'),
    path('<int:pk>', NewsDetail.as_view(), name='news'),
    path('search/', NewsSearch.as_view(), name='newssearch'),
    path('create/', NewsCreate.as_view(), name='newscreate'),
    path('articles/create/', ArticlesCreate.as_view(), name='articlescreate'),
    path('delete/<int:pk>/', PostDelete.as_view(), name='newsdelete'),
    path('edit/<int:pk>/', PostUpdate.as_view(), name='newsupdate'),
    path('author_edit/<int:pk>/', AuthorUpdate.as_view(), name='authorupdate'),
    path('subscribe/<int:pk>/', SubscribeUpdate.as_view(), name='subscribeupdate'),
    path('subscribe/create/', SubscribeCreate.as_view(), name='subscribecreate'),
    path('add_subscribe/<int:pk>/', add_subscribe, name='add_subscribe'),
    path('delete_subscribe/<int:pk>/', delete_subscribe, name='delete_subscribe'),
]
