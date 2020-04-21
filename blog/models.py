from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    comment_text = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.comment_text


class ChildComment(models.Model):
    comment_text = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    parent_comment = models.ForeignKey(Comment, related_name='child_comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='child_comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='child_comments', on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.comment_text
