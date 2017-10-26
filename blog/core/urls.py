from django.conf.urls import url
from .views import home, contact, about

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^contato/$', contact, name='contact'),
    url(r'^about/$', about, name='about'),
]