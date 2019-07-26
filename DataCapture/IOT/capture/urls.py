from django.conf.urls import url
from capture.views import index, capture_code

urlpatterns = [
    url(r'^$', capture_code, name='index'),
    url(r'^home$', index, name='Home'),
    ]