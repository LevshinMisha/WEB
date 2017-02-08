from django.conf.urls import url
from .views import main, next_stage

urlpatterns = [
    url(r'^$', main),
    url(r'nextStage/(?P<code_name>.+)$', next_stage)
]