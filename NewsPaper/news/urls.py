from django.urls import path
from .views import (
    NewsList, NewsDetail, NewsSearch, PostCreate, PostDelete, PostUpdate
)

urlpatterns = [
    path('', NewsList.as_view(), name='newslist'),
    path('<int:pk>', NewsDetail.as_view(), name='news'),
    path('search/', NewsSearch.as_view(), name='newssearch'),
    path('create/', PostCreate.as_view(), name='newscreate'),
    path('delete/<int:pk>/', PostDelete.as_view(), name='newsdelete'),
    path('edit/<int:pk>/', PostUpdate.as_view(), name='newsupdate'),
]
