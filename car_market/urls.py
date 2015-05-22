from django.conf.urls import include, url
from django.contrib import admin
from utils.views import IndexView


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),                          # import main admin urls
    url(r'^$', IndexView.as_view(), name='index'),                      # index view
    url(r'^accounts/', include('accounts.urls', namespace='accounts')), # import accounts urls
    url(r'^fabrics/', include('fabrics.urls', namespace='fabrics')),    # imports fabrics urls
    url(r'^admin_tools/', include('admin_tools.urls')),                 # import admin-tools url
]
