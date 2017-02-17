from django.conf.urls import url
from .views import main, next_stage, get_stage, current_stage

urlpatterns = [
    url(r'^$', main),
    url(r'nextStage/(?P<codename>.+)$', next_stage),
    url(r'getStage/(?P<codename>.+)$', get_stage),
    url(r'currentStage', current_stage)
]