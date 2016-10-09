from django.conf.urls import url
from .views import visits

urlpatterns = [
    url(r'^$', visits),
]