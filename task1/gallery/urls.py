from django.conf.urls import url
from .views import get_comments, gallery, add_comment

urlpatterns = [
    url(r'^$', gallery),
    url(r'^(?P<filename>[A-Za-z0-9.-_]*)/(?P<text>.*)', add_comment),
    url(r'^(?P<filename>[A-Za-z0-9.-_]*)', get_comments),

]

