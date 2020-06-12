from django.contrib import admin
from .models import BlogPost, Author, HomeBanner

# Register your models here.

admin.site.site_header = "Asif Blog Admin View"


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_of_publish',
                    'published', 'featured', 'author')
    list_filter = ['date_of_publish', 'published']
    search_fields = ['title']


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['user']


class HomeBannerAdmin(admin.ModelAdmin):
    list_filter = ['date', 'featured']


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(HomeBanner, HomeBannerAdmin)
