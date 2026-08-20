from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import user_login,user_logout,user_info,user_info_update

app_name = 'account'

urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', user_info, name='info'),
    path('profile/update/', user_info_update, name='update'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)