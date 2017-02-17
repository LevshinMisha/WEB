from django.conf.urls import url, include
from .views import main_page, about, links, contacts, redirect_to_main

urlpatterns = [
    url(r'^$', redirect_to_main),
    url(r'^main/', main_page),
    url(r'^about/', about),
    url(r'^links/', links),
    url(r'^contacts/', contacts),
    url(r'^gallery/', include('gallery.urls')),
    url(r'^feedbacks/', include('feedbacks.urls')),
    url(r'^visits/', include('visits.urls')),
    url(r'^game/', include('game.urls')),
    url(r'^chat/', include('chat.urls')),
]