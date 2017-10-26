from django.conf.urls import url
from .views import index, details

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^(?P<slug>[\w_-]+)/$', details, name='details')
]
