from django.conf.urls import *

from stocks.views import *

urlpatterns = [
    url(r'^$', stocks, name='stocks'),
    url(r'^pair_details/(?P<pair_id>\d+)/$', pair_details, name='pair_details'),
    url(r'^pair_list/$', pair_list, name='pair_list'),
    url(r'^accounts/(?P<account_slug>\w+)/$', account_details, name='account_details'),
    url(r'^accounts/(?P<account_slug>\w+)/take_snapshot/$', take_snapshot, name='take_snapshot'),
    url(r'^accounts/(?P<account_slug>\w+)/(?P<snapshot_number>\d+)/$', account_snapshot, name='account_snapshot'),
    url(r'^accounts/(?P<account_slug>\w+)/pair_transactions/$', account_pair_transactions, name='account_pair_transactions'),
]
