from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import candidates_list,candidate_info,candidate_to_employee,delete_candidate,edit_candidate

app_name = 'candidates'

urlpatterns = [
    path('', candidates_list, name='candidates'),
    path('candidate-info/', candidate_info, name='candidate-info'),
    path('candidate-to-employee/',candidate_to_employee,name='transfer-candidate'),
    path('delete/', delete_candidate, name='delete-candidate'),
    path('edit/', edit_candidate, name='edit-candidate'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)