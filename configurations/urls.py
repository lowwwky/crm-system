from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from CRMSystem.views import  PageNotFound

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('accounts.urls')),
    path('employees/',include('employees.urls')),
    path('hrcalendar/', include('hrcalendar.urls')),
    path('candidates/',include('candidates.urls')),
    path('', include('CRMSystem.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = PageNotFound