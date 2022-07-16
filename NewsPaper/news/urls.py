from django.urls import path
from .views import (
    NewsList, NewsDetail, NewsSearch, NewsCreate, PostDelete, PostUpdate, ArticlesCreate, AythorUpdate
)

urlpatterns = [
    path('', NewsList.as_view(), name='newslist'),
    path('<int:pk>', NewsDetail.as_view(), name='news'),
    path('search/', NewsSearch.as_view(), name='newssearch'),
    path('create/', NewsCreate.as_view(), name='newscreate'),
    path('articles/create/', ArticlesCreate.as_view(), name='articlescreate'),
    path('delete/<int:pk>/', PostDelete.as_view(), name='newsdelete'),
    path('edit/<int:pk>/', PostUpdate.as_view(), name='newsupdate'),
    path('author_edit/<int:pk>/', AythorUpdate.as_view(), name='authorupdate'),
]
