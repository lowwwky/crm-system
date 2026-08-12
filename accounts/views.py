from django.contrib.auth import login,logout
from django.shortcuts import render,redirect
from django.contrib import messages

from accounts.forms import LoginForm

def user_login(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        form = LoginForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Вы успешно зашли в аккаунт.')
            return redirect("calendar")
        else:
            messages.error(request, 'Неверное имя пользователя или пароль.')
            return render(request, 'accounts/login.html', {'form': form, 'title': 'Авторизация'})
    else:
        form = LoginForm()

    context = {
        'title': 'Авторизация пользователя',
        'form': form,
    }

    return render(request, 'accounts/login.html', context)

def user_logout(request):
    logout(request)
    messages.success(request,"Вы вышли из системы.")
    return redirect("accounts:login")




