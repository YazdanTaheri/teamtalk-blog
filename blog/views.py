from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment, Category
from .forms import CommentForm

# Display all posts
class PostList(generic.ListView):
    """
    Returns all published posts in :model:`blog.Post`
    and displays them in a page of six posts. 
    **Context**

    ``queryset``
        All published instances of :model:`blog.Post`
    ``paginate_by``
        Number of posts per page.
        
    **Template:**

    :template:`blog/index.html`
    """
    queryset = Post.objects.filter(status='published')
    template_name = "blog/index.html"
    paginate_by = 6

# Display all categories
def category_list(request):
    """
    Display a list of all categories.

    **Context**

    ``categories``
        All instances of :model:`blog.Category`.

    **Template:**

    :template:`blog/category_list.html`
    """
    categories = Category.objects.all()
    return render(request, 'blog/category_list.html', {'categories': categories})

# Display posts by category
def posts_by_category(request, category_id):
    """
    Display all posts under a specific :model:`blog.Category`.

    **Context**

    ``category``
        An instance of :model:`blog.Category`.
    ``posts``
        All posts linked to the category.

    **Template:**

    :template:`blog/posts_by_category.html`
    """
    category = get_object_or_404(Category, id=category_id)
    posts = category.posts.filter(status='published')
    return render(request, 'blog/posts_by_category.html', {'category': category, 'posts': posts})

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
def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.
    ``comments``
        All approved comments related to the post.
    ``comment_count``
        A count of approved comments related to the post.
    ``comment_form``
        An instance of :form:`blog.CommentForm`

    **Template:**

    :template:`blog/post_detail.html`
    """
    queryset = Post.objects.filter(status='published')
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    category = post.category
    comment_count = post.comments.filter(approved=True).count()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )
    
    comment_form = CommentForm()

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            'category': category,
            "comment_count": comment_count,
            "comment_form": comment_form
        },
    )

def comment_edit(request, slug, comment_id):
    """
    Display one comment for edit.

    **Context**
    ``post``
        An instance of :model:`blog.Post`.
    ``comment``
    A single comment related to the post.
    ``comment_form``
    An instance of :form:`blog.CommentForm`.
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status="published")
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    Display one comment to Delete.
    """
    queryset = Post.objects.filter(status="published")
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))
