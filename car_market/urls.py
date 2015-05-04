from django.conf.urls import include, url
from django.contrib import admin

from accounts.views import AccountRegistrationView


urlpatterns = [
    # Examples:
    # url(r'^$', 'car_market.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # url(r'^accounts/login$', login)
    url(r'register/$', AccountRegistrationView.as_view(), name='register')
]
