from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50, null=False)
    content = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    view_count = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/', null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


class Comment(models.Model):
    content = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    