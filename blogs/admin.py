from django.contrib import admin
from .models import Post, Category, Tag, User, Comment, Image


admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(User)
admin.site.register(Comment)
admin.site.register(Image)
