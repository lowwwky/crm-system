from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_not_required
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from accounts.forms import UserUpdateProfile
from accounts.models import UserProfile

@login_not_required
def user_login(request):
    if request.user.is_authenticated:
        return redirect("home:home-page")

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request,"Вы успешно вошли в аккаунт.")
            return redirect("home:home-page")
        else:
            messages.error(request,"Неверное имя пользователя или пароль.")
            return render(request, 'accounts/login.html', {'title':'Авторизация', 'form': form})

    form = AuthenticationForm()
    return render(request, "accounts/login.html", {
        'form':form,
        'title':"Авторизация пользователя"
    })

def user_logout(request):
    logout(request)
    messages.success(request,"Вы вышли из системы.")
    return redirect("account:login")


def user_info(request):
    profile, create = UserProfile.objects.get_or_create(
        user=request.user,
    )
    context ={
        'title': 'Страница пользователя',
        'profile_user': request.user,
        'user_profile': profile,
    }
    return render(request, 'accounts/profile.html', context=context)

def user_info_update(request):
    profile, create = UserProfile.objects.get_or_create(
        user=request.user,
    )
    if request.method == 'POST':
        form = UserUpdateProfile(request.POST, request.FILES,instance=profile, )
        print('FILES:', request.FILES)
        print('FORM FILES: ', form.files)
        print('FORM DATA: ', form.data)
        if form.is_valid():
            print('CLEANED:', form.cleaned_data)

            form.save()
            messages.success(request,'Профиль успешно обновлен.')
            return redirect("account:info")
    else:
        form = UserUpdateProfile(instance=profile)
    return render(request, 'accounts/update.html',{'form':form,})











