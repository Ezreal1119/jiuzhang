from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from appone.models import JiuzhangUser

# forms defined here handles user inputs

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = JiuzhangUser
        fields = ('username', 'email', 'profile_pic')