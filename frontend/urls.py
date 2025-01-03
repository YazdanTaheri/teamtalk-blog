from frontend.views import home


from django.contrib import admin
from django.urls import path, include
from frontend import views

urlpatterns = [
    path('', views.category_list, name='home'),
]