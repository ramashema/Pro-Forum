from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """The model class for forum posts"""
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """String representation of of Post"""
        return self.title


class Comment(models.Model):
    """The model class for comments posted on the posts"""
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """String representation of of the comments"""
        return f"{self.text[:100]}"
