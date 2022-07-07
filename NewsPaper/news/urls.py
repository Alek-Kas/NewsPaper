from django.urls import path
from .views import NewsList, NewsDetail, NewsSearch

urlpatterns = [
    path('', NewsList.as_view(), name='newslist'),
    path('<int:pk>', NewsDetail.as_view(), name='news'),
    path('search/', NewsSearch.as_view(), name='newssearch'),
    '''
    /news/create/
    /news/<int:pk>/edit/
    /news/<int:pk>/delete/
    /articles/create/
    /articles/<int:pk>/edit/
    /articles/<int:pk>/delete/
    '''
]
