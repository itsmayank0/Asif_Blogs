from django.shortcuts import render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import BlogPost, HomeBanner
from django.views.generic import DetailView


def Homepage(request, page=None):
    queryset1 = BlogPost.objects.filter(featured=True)
    queryset2 = HomeBanner.objects.filter(featured=True)
    paginator = Paginator(queryset1, 6)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    finally:
        context = {
            'posts': posts,
            'banner': queryset2
        }
    return render(request, 'index.html', context)


def blog(request):
    pass


def about(request):
    pass


def contact(request):
    pass
