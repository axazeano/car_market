from django.conf.urls import include, url
from .views import create_fabric, fabric_dashboard


urlpatterns = [
    url(r'^fabric_dashboard/?P<account_id>[0-9]+/$', fabric_dashboard, name='dashboard'),
    url(r'^create_fabric/$', create_fabric, name='create'),
]
