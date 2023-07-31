from django.shortcuts import render


# Create your views here.
from blog.models import Post


def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})


def post(request, post_id):
    posts = Post.objects.get(pk=post_id)
    return render(request, 'post.html', {'post': posts})
