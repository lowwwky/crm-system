from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import show_calendar,assign_new,day_detail,delete_detail,delete_all,event_detail

app_name = 'hrcalendar'

urlpatterns = [
    path('', show_calendar, name='index'),
    path('day-detail/', day_detail, name='events-of-the-day'),
    path('show-event-detail/',event_detail, name='event-details'),
    path('add-event/', assign_new, name='new-event'),
    path('delete-detail/', delete_detail, name='delete-event'),
    path('delete-all-day/', delete_all, name='delete-all-events-of-the-day'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)