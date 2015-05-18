from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.conf import settings
from django.shortcuts import render
from django.views.generic import FormView
from django.contrib.auth import (
    login as auth_login, logout as auth_logout, authenticate)

from .forms import UserCreateForm
from redis_manager.redis_manager import RedisUser


class AccountRegistrationView(FormView):
    template_name = 'accounts/registration.html'
    form_class = UserCreateForm
    success_url = '/'

    def form_valid(self, form):
        saved_user = form.save()
        user = authenticate(
            username=saved_user.username,
            password=form.cleaned_data['password1'])
        auth_login(self.request, user)
        RedisUser.login(user)
        return HttpResponseRedirect(self.get_success_url())


class LoginView(FormView):
    template_name = 'accounts/login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        user = form.get_user()
        auth_login(self.request, user)
        settings.REDIS.sadd('users_online', user)
        return super(LoginView, self).form_valid(form)


@login_required
def dashboard_view(request):
    messages = RedisUser.get_messages(request.user)
    context = {'user': request.user,
               'messages': messages}
    return render(request, 'accounts/dashboard.html', context)


@login_required
def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('login'))


