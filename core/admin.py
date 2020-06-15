from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models
from django.db.models.functions import Lower
from .models import BlogPost, Author, HomeBanner, Queries

# Register your models here.


admin.site.site_header = "Asif Blog Admin View"


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_of_publish',
                    'public', 'featured', 'author')
    list_filter = ['date_of_publish', 'published', 'public']
    search_fields = ['title']

    fieldsets = [
        ("Post Details", {'fields': [
         "title", "overview", "thumbnail", "date_of_publish", "published", "author", "featured", "youtube", 'public']}),
        ("Content", {"fields": ["post_content"]})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }

    def get_ordering(self, request):
        return [Lower('date_of_publish')]


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['user']


class HomeBannerAdmin(admin.ModelAdmin):
    list_filter = ['date', 'featured']


class QueriesAdmin(admin.ModelAdmin):
    list_display = ['author_name', 'author_email', 'solved_status']
    list_filter = ['solved_status']


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(HomeBanner, HomeBannerAdmin)
admin.site.register(Queries, QueriesAdmin)
