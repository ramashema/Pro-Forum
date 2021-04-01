from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.contrib import messages

from .models import Post, Comment
from .forms import PostForm, CommentForm


def index(request):
    """The view function to load the home page"""
    return render(request, 'posts/index.html')


def posts(request):
    """The view function to display forum posts"""
    forum_posts = Post.objects.order_by('-date_added')
    context = {'forum_posts': forum_posts}

    return render(request, 'posts/posts.html', context)


def post(request, post_id):
    """The view function for post details"""
    forum_post = Post.objects.get(id=post_id)
    post_comments = forum_post.comment_set.order_by('-date_added')
    context = {'forum_post': forum_post, 'post_comments': post_comments}

    return render(request, 'posts/post.html', context)


@login_required
def new_post(request):
    """The view function to add new post"""
    if request.method != 'POST':
        form = PostForm()
    else:
        form = PostForm(request.POST)
        if form.is_valid():
            # check if data is valid
            newpost = form.save(commit=False)
            newpost.owner = request.user
            newpost.save()
        messages.add_message(request, messages.SUCCESS, 'Post successfully added')
        return redirect('posts:posts')
    
    context = {'form': form}
    return render(request, 'posts/new_post.html', context)


@login_required
def new_comment(request, post_id):
    """The view function to add new comment"""
    post = Post.objects.get(id=post_id)

    if request.method != 'POST':
        form = CommentForm()
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            # check if the data passed validation 
            newcomment = form.save(commit=False)
            newcomment.post = post
            newcomment.owner = request.user
            newcomment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment successfully added')
            return redirect("posts:post", post_id=post_id)
    
    context = {'form': form, 'post': post}
    return render(request, 'posts/new_comment.html', context)


@login_required
def edit_comment(request, comment_id):
    """The view function to edit existing comment"""
    comment = Comment.objects.get(id=comment_id)

    if comment.owner != request.user:
        raise Http404

    post = comment.post

    if request.method != 'POST':
        form = CommentForm(instance=comment)
    else:
        form = CommentForm(instance=comment, data=request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Post successfully updated')
            return redirect('posts:post', post_id=post.id)

    context = {'form': form, 'post': post, 'comment': comment}
    return render(request, 'posts/edit_comment.html', context)


@login_required
def edit_post(request, post_id):
    """The view function to edit existing post"""
    post = Post.objects.get(id=post_id)

    if post.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = PostForm(instance=post)
    else:
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Post successfully updated')
            return redirect('posts:post', post_id=post_id)

    context = {'form': form, 'post': post}
    return render(request, 'posts/edit_post.html', context)


@login_required
def delete_post(request, post_id):
    """The view function to delete existing post"""
    posts = Post.objects.order_by('-date_added')
    post = Post.objects.get(id=post_id)

    if post.owner != request.user:
        raise Http404

    if post.delete():
        messages.add_message(request, messages.SUCCESS, 'You have successfully deleted your post')
    else:
        messages.add_message(request, messages.ERROR, 'There is a problem when trying to delete the post')

    context = {'forum_posts': posts}
    return render(request, 'posts/posts.html', context)
    

@login_required
def delete_comment(request, comment_id):
    """The view function to delete the post comment"""
    comment = Comment.objects.get(id=comment_id)
    forum_post = comment.post
    post_comments = forum_post.comment_set.order_by('-date_added')

    if comment.delete():
        messages.add_message(request, messages.SUCCESS, 'You have successfully deleted your comment') 
    else:
        messages.add_message(request, messages.ERROR, 'There is a problem when trying to delete the comment')


    context = {'forum_post': forum_post, 'post_comments': post_comments}
    return render(request, 'posts/post.html', context)







