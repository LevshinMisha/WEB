from django.conf.urls import url, include
from .views import main_page, about, links, contacts, gallery, popup, homework

urlpatterns = [
    url(r'^$', main_page),
    url(r'^about/', about),
    url(r'^links/', links),
    url(r'^contacts/', contacts),
    url(r'^gallery/', gallery),
    url(r'^feedbacks/', include('feedbacks.urls')),
    url(r'^popup/', popup),
    url(r'^visits/', include('visits.urls')),
    url(r'^homework/', homework)
]