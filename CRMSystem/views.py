from django.contrib.auth.decorators import login_not_required
from django.contrib.auth.forms import AuthenticationForm
from django.http.response import HttpResponseNotFound
from django.shortcuts import render

def main_page(request):
    if request.user.is_authenticated:
        return render(request, 'CRMSystem/home.html')

    form = AuthenticationForm()
    return render(request, "accounts/login.html", {
        'form': form,
        'title': "Авторизация пользователя"
    })

@login_not_required
def PageNotFound(request, exception, *args, **kwargs):
    return HttpResponseNotFound('Страница не найдна')