from django.urls import path
from . import views

urlpatterns = [
    path('',views.blog_list, name='blog_list'),
    path('blog/writing', views.blog_writing, name='blog_writing'),
]