from django.conf.urls import url

from .views import image_view


urlpatterns = [
    url(
        r'^(?P<operation>\w+)/(?P<size>\w+)/(?P<optional_parameters>[\w\.\,\;-]+)/(?P<path>.+)$',
        image_view,
        name='cloudimage_image',
    ),
]
