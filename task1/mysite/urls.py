from django.conf.urls import url, include
from django.contrib import admin
from .views import main_page, about, links, pictures, contacts, log_in

urlpatterns = [
    url(r'^$', main_page),
    url(r'^about/', about),
    url(r'^links/', links),
    url(r'^pictures/', pictures),
    url(r'^contacts/', contacts),
    url(r'^login/', log_in)
]