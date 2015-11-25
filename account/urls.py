from django.conf.urls import url
from account.views import *


urlpatterns = [
    url(r'^create/$', 'account.views.create_user'),
    url(r'^getuser/$', 'account.views.get_user'),
    url(r'^updateprofile/$', 'account.views.update_user_profile'),
]
