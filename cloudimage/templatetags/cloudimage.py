from django import template
from django.conf import settings
from django.urls import reverse


register = template.Library()


@register.simple_tag
def image(img, operation, size, optional_parameters):
    if not img:
        if settings.DEBUG:
            raise ValueError('No image path defined')
        return ''

    return reverse('cloudimage_image', kwargs={
        'operation': operation,
        'size': size,
        'optional_parameters': optional_parameters,
        'path': img,
    })
