from django.urls import path
from . import views


app_name = 'blogs'
urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('category/', views.CategoryListView.as_view(), name='category_list'),
    path('category/<int:pk>/', views.PostListView.as_view(), name='post_list')
]
