from django.conf.urls import url
from .views import AccountRegistrationView, LoginView, logout, dashboard_view


urlpatterns = [
    url(r'^registration/$', AccountRegistrationView.as_view(), name='registration'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^dashboard/$', dashboard_view, name='dashboard'),
    url(r'^logout/$', logout, name='logout'),
]