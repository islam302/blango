from django.shortcuts import render, redirect
from blog.models import Post  # Import the Post model
from blog.forms import CommentForm

def index(request):
    post = None  # Initialize the variable 'post'

    if request.user.is_active:
        if request.method == "POST":
            comment_form = CommentForm(request.POST)

            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.content_object = post
                comment.creator = request.user
                comment.save()
                return redirect(request.path_info)
        else:
            comment_form = CommentForm()
        
        # Fetch a post from the database (adjust as needed based on your model)
        post = Post.objects.first()
    else:
        comment_form = None
    
    return render(
        request, "blog/post-detail.html", {"post": post, "comment_form": comment_form}
    )
