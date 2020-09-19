from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_info(request, pk):
    post = get_object_or_404(Post, id=pk)
    return render(request, 'blog/post_info.html', {
        "post": post
        })