from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Post, Category, Tag, User, Comment, PostStatus


# admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(User)
admin.site.register(Comment)
admin.site.register(PostStatus)

# django-markdownxのエディタ
admin.site.register(Post, MarkdownxModelAdmin)
