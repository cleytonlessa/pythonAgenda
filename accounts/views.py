from email import message
from django.shortcuts import render
from django.contrib import messages


def login(request):
    return render(request, 'accounts/login.html')


def logout(request):
    return render(request, 'accounts/logout.html')


def cadastro(request):
    #messages.success(request, 'Olá mundo')
    # print(request.POST)
    return render(request, 'accounts/cadastro.html')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')
