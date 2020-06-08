from django.urls import path
from .views import home_page_view, show_blog

urlpatterns = [
    path('', home_page_view, name="home_view"),
    path('showblog/', show_blog, name="show_blog"),
]
