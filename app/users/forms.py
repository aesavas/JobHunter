from django import forms
from django.contrib.auth.forms import UserCreationForm

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
