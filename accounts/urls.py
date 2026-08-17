from django.urls import path
from .views import user_login,user_logout,user_info

app_name = 'account'

urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', user_info, name='info'),
]