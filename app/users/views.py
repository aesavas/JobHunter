from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.views import PasswordChangeView

#! Forms
from .forms import CustomUserCreationForm, SkillCreationForm

#! Models
from .models import User

# Create your views here.

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


def edit_account_view(request):
    profile = request.user.profile
    if request.method == "POST":
        new_name = request.POST['name']
        new_email = request.POST['email']
        profile.name = new_name
        profile.email = new_email
        profile.user.username = new_email
        #TODO : This solution is not professional. We need to find something better.
        try:
            new_profile_picture = request.FILES['profile-picture']
            profile.profile_image = new_profile_picture
        except:
            pass
        profile.save()
        messages.success(request, 'Your profile have been updated successfully!')
        return redirect('dashboard:dashboard')
    return render(request, 'users/edit-account.html', {'profile':profile})


def edit_password_view(request):
    profile = request.user.profile
    if request.method == "POST":
        currentPassword = request.POST['current-password']
        if check_password(currentPassword, profile.user.password):
            newPassword = request.POST['new-password']
            newPassword2 = request.POST['new-password2']
            if newPassword and newPassword2 and newPassword == newPassword2:
                profile.user.set_password(newPassword)
                profile.save()
                update_session_auth_hash(request, profile.user)
                messages.warning(request, 'Your password has been changed successfully!')
                return redirect('dashboard:dashboard')
    return render(request, 'users/edit-password.html')


def add_skill_view(request):
    form = SkillCreationForm()
    if request.method == "POST":
        form = SkillCreationForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = request.user.profile
            skill.save()
            messages.success(request, 'Your skill has been added successfully!')
            return redirect('account:account')

    context = {
        'form':form,
    }
    return render(request, 'users/add-skill.html', context)