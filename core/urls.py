from django.urls import path
from .views import blog, about, contact, Homepage

urlpatterns = [
    path('', Homepage, name="home_view"),
    path('blog/', blog, name="show_blog"),
    path('about/', about, name="about"),
    path('contact/', contact, name="contact"),
]
