from django.shortcuts import render

from .models import Post


# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

