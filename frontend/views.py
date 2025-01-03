from django.http import HttpResponse
from blog.models import Category
from django.shortcuts import render

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
