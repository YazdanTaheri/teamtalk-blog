from frontend.views import home


from django.contrib import admin
from django.urls import path, include
from frontend import views


urlpatterns = [
    path('', views.category_list, name='home'),
    path('blog/category/<int:category_id>/', views.posts_by_category, name='posts_by_category'),
    path('blog/category/<slug:slug>/', views.category_list, name='category_list'),
]