from django.urls import path
from .views import article_list, article_create, article_delete

urlpatterns = [
    path('', article_list, name='article_list'),
    path('article/new/', article_create, name='article_create'),
    path('article/<int:pk>/delete/', article_delete, name='article_delete'),
]
