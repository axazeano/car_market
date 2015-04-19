__author__ = 'vladimir'

from django import forms


class Login(forms.Form):
    username = forms.CharField(label='username', max_length=100, required=True)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)