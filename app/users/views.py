from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

#! Forms
from .forms import CustomUserCreationForm

#! Models
from .models import User

# Create your views here.
"""
TODO : View List
- Account
- Edit Account
- Change Password?
"""

def sign_up_view(request):
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User account was created successfully!')
            return redirect('')
    return render(request, 'users/sign-up.html', {'form':form,})


def login_view(request):
    form = CustomUserCreationForm()
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get('username')
        except:
            messages.error(request, 'Username does not exist!')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print('SUCCESS')
            messages.success(request, 'User has been login successfully!')
            return redirect('dashboard:dashboard')
        else:
            messages.error(request, 'Username or password is incorrect!')
    return render(request, 'users/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request, 'User was logged out successfully.')
    return redirect('landing-page')

def account_view(request):
    return render(request, 'users/account.html', {'profile':request.user.profile})