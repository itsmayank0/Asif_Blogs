from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('', include('core.urls')),
    path('aboutUs/', include('core.urls')),
    path('recentblogs/', include('core.urls')),
    path('contactUs/', include('core.urls')),
    path('article/<slug:slug>', include('core.urls')),
    path('submit/', include('Marketing.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
