from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm, SetPasswordForm

from .models import User, Skill


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'username', 'password1', 'password2']
        labels = {
            'first_name': 'Name',
            'username': 'Email'
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})

    def save(self, commit=True):
        """
            I am using Django's base password reset system. So if I do not save the user email, the system doesn't send reset email.
        """
        user = super().save(commit=False)
        user.email = self.cleaned_data["username"]
        if commit:
            user.save()
        return user


class SkillCreationForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'badge_color']
        labels = {
            'name' : 'Name',
            'badge_color' : 'Badge Color'
        }

    def __init__(self, *args, **kwargs):
        super(SkillCreationForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})


class UserPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(UserPasswordResetForm, self).__init__(*args, **kwargs)

    email = forms.EmailField(label='Email',widget=forms.EmailInput(attrs={
            'class':'form-control',
            'placeholder':'Enter your email please..',
            'type':'email',
            'name':'email'
        }))

class UserPasswordSetForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(UserPasswordSetForm, self).__init__(*args, **kwargs)

    new_password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Enter your new password',
    }))

    new_password2 = forms.CharField(label="Password Confirmation", widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Retype your new password',
    }))