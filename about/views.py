from django.shortcuts import render
from django.contrib import messages
from .models import About

# Create your views here.


def about_me(request):
    """
    Renders the most recent information on the website author
    and allows user collaboration requests.

    Displays an individual instance of :model:`about.About`.

    **Context**
    ``about``
        The most recent instance of :model:`about.About`.
        ``collaborate_form``
            An instance of :form:`about.CollaborateForm`.
    
    **Template**
    :template:`about/about.html`
    """

     # Ensure 'about' is properly defined
    about = About.objects.order_by('-updated_on').first()

    return render(
        request,
        "about/about.html",
        {"about": about},
    )