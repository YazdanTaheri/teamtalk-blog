from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm  

# Display all posts
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})

# Create a new post
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new post to the database
            return redirect('index.html')  # Redirect to the list of posts after saving
    else:
        form = PostForm()  # If it's a GET request, show an empty form

    return render(request, 'blog/index.html', {'form': form})

# View a single post
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/index.html', {'post': post})
