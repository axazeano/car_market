from django.shortcuts import render
from django.http import HttpResponse
from .forms import Login


def login(request):
    form = Login()
    return render(request, 'accounts/login.html', {'form': form})