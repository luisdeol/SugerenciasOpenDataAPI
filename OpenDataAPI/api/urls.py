from django.conf.urls import patterns, url

urlpatterns = patterns(
    'api.views',
    url(r'^get_All_SugRec/$', 'get_All_SugRec', name='get_All_SugRec'),
)