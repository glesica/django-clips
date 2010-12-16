from django.conf.urls.defaults import *

from clips.views import clip_list, tag_list, clip

urlpatterns = patterns('',
    (r'^$', clip_list, {'home': True}),
    (r'^index/$', tag_list),
    (r'^concept/(?P<tag_slug>[a-zA-Z0-9_-]+)/$', clip_list),
    (r'^clip/(?P<clip_id>\d+)/$', clip),
    (r'^contributor/(?P<credit_id>\d+)/$', clip_list),
)
