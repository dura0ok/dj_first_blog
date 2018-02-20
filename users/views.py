from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from .forms import Login
from blog.models import Client

# test


def register(request):
    test = ''
    form = UserCreationForm

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            test = 'Успешно, теперь войдите'

    context = {
        'form': form,
        'test': test,
        'title': 'Регистрация'
    }

    return render(request, 'register.html', context=context)


def login(request):
    form = Login
    status_login = ''
    if request.method == 'POST':
        form = Login(request.POST)
        if form.is_valid():
            user_login = auth.authenticate(username=form.cleaned_data['username'],
                                           password=form.cleaned_data['password'])
            if user_login is not None and user_login.is_active:
                auth.login(request, user_login)
                request.session['user'] = form.cleaned_data['username']
                return redirect('/')
            else:
                status_login = 'Неправильный логин или пароль'
    context = {
        'status': status_login,
        'form': form,
        'title': 'Вход'
    }
    return render(request, 'login.html', context=context)

def logout(request):
    auth.logout(request)
    return redirect('/')
