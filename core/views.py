from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import BlogPost, HomeBanner, Queries, Author
from django.views.generic import DetailView
from django.contrib import messages
from django.http import HttpResponseRedirect


def Homepage(request, page=None):
    queryset1 = BlogPost.objects.filter(featured=True, public=True)
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


def article_detail(request, slug):
    queryset1 = BlogPost.objects.filter(
        slug=slug)
    queryset2 = BlogPost.objects.order_by('date_of_publish')[0:3]
    context = {
        'post': queryset1,
        'latest_post': queryset2,
    }
    return render(request, 'post-page.html', context)


def aboutUs(request):
    return render(request, 'aboutUs.html')


def contactUs(request):
    if request.method == "GET":
        return render(request, 'contactUs.html')
    else:
        author_name = request.POST['author_name']
        author_email = request.POST['author_email']
        message = request.POST['message']
        obj = Queries(author_name=author_name,
                      author_email=author_email, message=message, solved_status=False)
        obj.save()
        messages.info(request, " We Will catch You Soon🧐..")
        return render(request, "contactUs.html")


def recent_blogs(request):
    queryset1 = BlogPost.objects.all().order_by('date_of_publish')
    paginator = Paginator(queryset1, 3)
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
        }
    return render(request, 'recentBlogs.html', context)
