from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

def user_login(request):
    if request.user.is_authenticated:
        return redirect('main')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request,"Вы успешно вошли в аккаунт.")
            return redirect("main")
        else:
            messages.error(request,"Неверное имя пользователя или пароль.")
            return render(request, 'login.html', {'title':'Авторизация', 'form': form})

    form = AuthenticationForm()
    return render(request, "login.html", {
        'form':form,
        'title':"Авторизация пользователя"
    })

def user_logout(request):
    logout(request)
    messages.success(request,"Вы вышли из системы.")
    return redirect("main")

@login_required(login_url='/accounts/login/')
def user_info(request):
    return render(request, 'accounts/profile.html', {'title':'Страница пользователя', 'profile_user': request.user})

@login_required(login_url='/accounts/login/')
def user_info_update(request):
    pass








