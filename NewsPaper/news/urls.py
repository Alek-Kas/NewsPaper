from django.urls import path
# from .views import ProductsList, ProductDetail
from .views import NewsList, NewsDetail

urlpatterns = [
   # path('', ProductsList.as_view()),
   # path('<int:pk>', ProductDetail.as_view()),
    path('', NewsList.as_view()),
    path('<int:pk>', NewsDetail.as_view()),
]