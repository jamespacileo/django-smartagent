from django.conf.urls.defaults import *

from smartagent.views import force_desktop_version, unforce_desktop_version

urlpatterns = patterns('',
    url(r'^force_desktop_version/$', force_desktop_version, name="force_desktop_version"),
    url(r'^unforce_desktop_version/$', unforce_desktop_version, name="unforce_desktop_version"),
)