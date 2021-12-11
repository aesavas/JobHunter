from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages

#! Forms
from .forms import CustomUserCreationForm

# Create your views here.
"""
TODO : View List
- Register
- Login
- Logout
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
        