from django.contrib import admin
from .models import EmailList

# Register your models here.


class EmailListAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'user_email')
    list_filter = ['user_name']
    search_fields = ['user_name', 'user_email']


admin.site.register(EmailList, EmailListAdmin)
