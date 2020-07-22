from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
import pdb

# Create your views here.
def new(request):
    return render(request, 'posts/new.html')


def create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        Post.objects.create(title=title, content=content, image=image)
    return redirect('posts:main')


def main(request):
    posts = Post.objects.all()
    return render(request, 'posts/main.html', {'posts': posts})


def show(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'posts/show.html', {'post': post})


def update(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        # pdb.set_trace()
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.image = request.FILES.get('image')
        post.save()
        return redirect('posts:show', post.id)
    return render(request, 'posts/edit.html', {"post": post})


def delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('posts:main')