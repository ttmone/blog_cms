from django.urls import path
from . import views


app_name = 'blogs'
urlpatterns = [
    path('', views.PostIndexView.as_view(), name='index'),
    path('post/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('category/', views.CategoryListView.as_view(), name='category_list'),
    path('category/<int:pk>/', views.CategoryView.as_view(), name='category'),
    path('tag/', views.TagListView.as_view(), name='tag_list'),
    path('tag/<int:pk>', views.TagView.as_view(), name='tag'),
]
