from django.urls import path
from .views import NewsList, NewsDetail, NewsSearch, NewsCreate

urlpatterns = [
    path('', NewsList.as_view(), name='newslist'),
    path('<int:pk>', NewsDetail.as_view(), name='news'),
    path('search/', NewsSearch.as_view(), name='newssearch'),
    path('create/', NewsCreate.as_view(), name='newscreate'),
]
