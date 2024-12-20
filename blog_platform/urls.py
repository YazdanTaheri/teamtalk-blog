"""
URL configuration for blog_platform project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from about import views as about_views

urlpatterns = [
    path('about/', about_views.about_me, name='about'),
    path("accounts/", include("allauth.urls")),
    path('blog/', include("blog.urls"), name='blog-urls'),  # Blog URLs under '/blog/'
    path('admin/', admin.site.urls),
    path('', lambda request: render(request, 'frontend/index.html'), name='home'),  # Root URL
    path("summernote/", include("django_summernote.urls")),
]
