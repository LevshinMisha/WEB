from django.conf.urls import url
from .views import main, messages, add_message, last_message

urlpatterns = [
    url(r'^$', main),
    url(r'messages', messages),
    url(r'addMessage/(?P<text>.+)', add_message),
    url(r'lastMessage', last_message)
]