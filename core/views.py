from django.shortcuts import render
from .models import BlogPost

# Create your views here.


def home_page_view(request):
    return render(request, 'index.html')


def show_blog(request):
    post = BlogPost.objects.get(title='demo')
    return render(request, 'oneBlog.html', {'post': post})
