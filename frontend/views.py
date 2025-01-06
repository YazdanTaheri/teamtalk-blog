from django.http import HttpResponse
from blog.models import Category, Post
from django.shortcuts import render, get_object_or_404

def home(request):
    if request.method =="POST":
        return HttpResponse("Hello Home!")
    else:
        return HttpResponse(request.method)


def category_list(request):
    """
    A view to return the category list on the home page
    """
    categories = Category.objects.all()

    context = {
        'categories': categories,
    }
    return render(request, 'frontend/index.html', context)

def posts_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = Post.objects.filter(category=category)
    return render(request, 'blog/posts_by_category.html', {'category': category, 'posts': posts})