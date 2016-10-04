from django.conf.urls import url
from .views import main_page, about, links, contacts, gallery

urlpatterns = [
    url(r'^$', main_page),
    url(r'^about/', about),
    url(r'^links/', links),
    url(r'^contacts/', contacts),
    url(r'^gallery/', gallery)
]