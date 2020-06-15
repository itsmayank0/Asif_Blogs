from django.urls import path
from .views import article_detail, aboutUs, contactUs, Homepage, recent_blogs

urlpatterns = [
    path('', Homepage, name="home_view"),
    path('recentblogs/', recent_blogs, name="show_blog"),
    path('aboutUs/', aboutUs, name="about"),
    path('contactUs/', contactUs, name="contact"),
    path('contactUs/submit', contactUs, name="contact"),
    path('article/<slug:slug>', article_detail, name="article"),
]
