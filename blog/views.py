from django.shortcuts import render, redirect
from blog.models import Post 
from blog.forms import CommentForm


def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    
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

    return render(request, "blog/post-detail.html", {"post": post, "comment_form": comment_form})
