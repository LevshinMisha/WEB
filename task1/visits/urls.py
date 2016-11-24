from django.conf.urls import url
from .views import visits, visits_img

urlpatterns = [
    url(r'^$', visits),
    url(r'^img/(?P<url>.*)', visits_img)
]