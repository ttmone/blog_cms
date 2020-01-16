from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post, Category


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.kwargs:
            queryset = queryset.filter(category__pk=self.kwargs['pk'])
        return queryset


class PostDetail(DetailView):
    model = Post


class CategoryListView(ListView):
    model = Category
    context_object_name = 'categories'


# class CategoryPostListView(ListView):
#     model = Post
#     context_object_name = 'posts'
#
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         queryset = queryset.filter(category__pk=self.kwargs['pk'])
#         return queryset
