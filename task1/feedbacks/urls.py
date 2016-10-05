from django.conf.urls import url
from .views import feedback_main, feedback_new, feedback_edit, feedback_delete, cheater

urlpatterns = [
    url(r'^$', feedback_main, name='feedback_main'),
    url(r'^new/$', feedback_new, name='feedback_new'),
    url(r'^(?P<pk>[0-9]+)/edit/$', feedback_edit, name='feedback_edit'),
    url(r'^(?P<pk>[0-9]+)/delete/$', feedback_delete, name='feedback_delete'),
    url(r'^cheater$', cheater, name='feedback_cheater')
]