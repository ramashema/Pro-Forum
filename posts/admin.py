from django.contrib import admin
from .models import Post, Comment


class CommentInLine(admin.TabularInline):
    """Display comments inside post model in admin"""
    model = Comment


class PostAdmin(admin.ModelAdmin):
    """Topic model in the admin page"""
    inlines = [
        CommentInLine
    ]

    list_display = ('title', 'date_added')


admin.site.register(Post, PostAdmin)

