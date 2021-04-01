"""Urls patterns form posts app"""

from django.urls import path
from . import views


app_name = "posts"

urlpatterns = [
    path('', views.index, name='home'),  # home page
    path('posts', views.posts, name='posts'),  # posts page
    path('posts/<int:post_id>', views.post, name='post'),  # post page
    path('new_post/', views.new_post, name='new_post'), # add new post
    path('new_comment/<int:post_id>', views.new_comment, name='new_comment' ), # add new comment
    path('edit_comment/<int:comment_id>', views.edit_comment, name='edit_comment'), # edit the comment
    path('delete_comment/<int:comment_id>', views.delete_comment, name='delete_comment'), # delete comment 
    path('edit_post/<int:post_id>', views.edit_post, name='edit_post'), # edit post
    path('delete_post/<int:post_id>', views.delete_post, name='delete_post'), # delete post
]
