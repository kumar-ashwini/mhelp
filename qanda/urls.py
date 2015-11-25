from django.conf.urls import url
from qanda.views import *


urlpatterns = [
    url(r'^createquestion/$', 'qanda.views.create_question'),
    url(r'^createanswer/$', 'qanda.views.create_answer'),
    url(r'^getallquestion/$', 'qanda.views.get_all_questions'),
    url(r'^getmyquestion/$', 'qanda.views.get_my_questions'),
    url(r'^getallanswer/$', 'qanda.views.get_all_answer'),
    



]