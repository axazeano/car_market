from django.http import HttpResponseRedirect

from django.views.generic import FormView
from django.contrib.auth import (
    login as auth_login, authenticate)

from .forms import UserCreateForm


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
        return HttpResponseRedirect(self.get_success_url())
