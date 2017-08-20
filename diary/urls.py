from django.conf.urls import *

from diary.views import *

urlpatterns = [
    url(r'^$', diary_index, name='diary_index'),
    url(r'^list/$', diary_list, name='diary_list'),
    url(r'^details/(?P<diary_id>\d+)/$', diary_details, name='diary_details'),
    url(r'^details/(?P<diary_id>\d+)/add_text/$', diary_add_text, name='diary_add_text'),
    url(r'^details/(?P<diary_id>\d+)/add_image/$', diary_add_image, name='diary_add_image'),
    url(r'^edit_text/(?P<content_id>\d+)/$', diary_edit_text, name='diary_edit_text'),
]
