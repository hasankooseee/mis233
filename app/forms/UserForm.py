from django import forms
from django.contrib.auth import models
from django.core.exceptions import ValidationError


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = models.User
        fields = ['username', 'password']
