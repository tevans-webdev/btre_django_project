from django.shortcuts import render, redirect
from django.contrib import messages


def registerPage(request):
    if request.method == 'POST':
        # register user
        messages.error(request, 'Testing error message')
        return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def loginPage(request):
    if request.method == 'POST':
        # login user
        pass
    else:
        return render(request, 'accounts/login.html')


def logoutPage(request):
    return redirect('index')


def dashboardPage(request):
    return render(request, 'accounts/dashboard.html')
