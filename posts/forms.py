from django import forms

from .models import Post, Comment


class PostForm(forms.ModelForm):
    """This is form class for forum post"""
    class Meta:
        model = Post
        fields = ['title', 'body']
        labels = {'title': 'Title', 'body': 'Body'}
        widget = {'title': forms.TextInput(attrs={'placeholder': 'Post title'}), 'body': forms.Textarea(attrs={'col':80})}


class CommentForm(forms.ModelForm):
    """This is the form class for post comment"""
    class Meta:
        model = Comment
        fields = ['text']
        labels = {'text': 'Comment'}
        widget = {'text': forms.Textarea(attrs={'col': 80})}