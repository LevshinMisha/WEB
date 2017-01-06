from django.conf.urls import url
from .views import get_comments, gallery, add_comment, like, get_likes, get_xls

urlpatterns = [
    url(r'^$', gallery),
    url(r'^addComment/(?P<filename>[A-Za-z0-9.-_]*)/(?P<text>.*)', add_comment),
    url(r'^getComments/(?P<filename>[A-Za-z0-9.-_]*)', get_comments),
    url(r'^like/(?P<filename>[A-Za-z0-9.-_]*)', like),
    url(r'^getLikes/(?P<filename>[A-Za-z0-9.-_]*)', get_likes),
    url(r'^xls', get_xls)

]

