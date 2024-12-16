from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),  # Post list view
    path('post/new/', views.post_create, name='post_create'),  # New post view
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]

