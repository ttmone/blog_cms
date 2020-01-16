from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post, Category


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'


class PostDetail(DetailView):
    model = Post


class CategoryListView(ListView):
    model = Category
    context_object_name = 'categories'


# class CategoryPostListView(ListView):
#     model = Post
