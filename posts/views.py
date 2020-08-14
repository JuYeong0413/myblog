from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment

# Create your views here.
def new(request):
    return render(request, 'posts/new.html')


def create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        writer = request.user
        image = request.FILES.get('image')
        Post.objects.create(title=title, content=content, writer=writer, image=image)
    return redirect('posts:main')


def main(request):
    posts = Post.objects.all()
    return render(request, 'posts/main.html', {'posts': posts})


def show(request, post_id):
    post = Post.objects.get(pk=post_id)
    post.view_count += 1
    post.save()
    all_comments = post.comments.all().order_by('-created_at')
    return render(request, 'posts/show.html', {'post': post, 'comments': all_comments })


def update(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
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


def create_comment(request, post_id):
    if request.method == "POST":
        post = get_object_or_404(Post, pk=post_id)
        current_user = request.user
        comment_content = request.POST.get('content')
        Comment.objects.create(content=comment_content, writer=current_user, post=post)
    return redirect('posts:show', post.pk)