
from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path('accounts/', include('django.contrib.auth.urls')),  # login, logout, password reset

    path('admin/', admin.site.urls),
    path('', include('dashboard.urls', namespace='dashboard')),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
