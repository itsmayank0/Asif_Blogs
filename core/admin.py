from django.contrib import admin
from .models import BlogPost, EmailList

# Register your models here.

admin.site.site_header = "Asif Blog Admin View"


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_of_publish', 'published', 'author_name')
    list_filter = ['date_of_publish', 'published']
    search_fields = ['title', 'author_name']


class EmailListAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'user_email')
    list_filter = ['user_name']
    search_fields = ['user_name', 'user_email']


admin.site.register(BlogPost, BlogPostAdmin)

admin.site.register(EmailList, EmailListAdmin)
