from django.conf.urls import include, url
from django.contrib import admin

from accounts.views import AccountRegistrationView, LoginView, logout, dashboard_view


urlpatterns = [
    # Examples:
    # url(r'^$', 'car_market.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # url(r'^accounts/login$', login)
    url(r'^accounts/register/$', AccountRegistrationView.as_view(), name='register'),
    url(r'^accounts/login/$', LoginView.as_view(), name='login'),
    url(r'^accounts/dashboard/$', dashboard_view, name='dashboard'),
    url(r'^accounts/logout/$', logout, name='logout')
]
