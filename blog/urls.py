from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [ 
    path('categories/', views.category_list, name='category_list'),
    path('categories/add/', views.add_category, name='add_category'),
    path('categories/edit/<int:pk>/', views.edit_category, name='edit_category'),
    path('categories/delete/<int:pk>/', views.delete_category, name='delete_category'),
    path('categories/<int:category_id>/', views.posts_by_category, name='posts_by_category'),
    path('',views.PostList.as_view(), name='posts'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
]

