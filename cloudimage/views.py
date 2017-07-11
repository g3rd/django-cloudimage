import requests
from io import BytesIO

from django.conf import settings
from django.http import Http404
from django.http import HttpResponse
from django.views.decorators.http import require_safe


@require_safe
def image_view(request, operation=None, size=None, optional_parameters=None, path=None):
    if not path:
        raise Http404('No path provided')

    if not hasattr(settings, 'CLOUDIMAGE_TOKEN'):
        raise Http404('No CloudImage.io token provided.')

    # Build the URL
    url = 'http://{token}.cloudimg.io/{operation}/{size}/{optional_parameters}/{path}'.format(
        token=settings.CLOUDIMAGE_TOKEN,
        operation=operation,
        size=size,
        optional_parameters=optional_parameters,
        path=path,
    )

    print(url)

    # Grab the image
    cloudimage_response = requests.get(url)

    # Return
    buffer_image = BytesIO(cloudimage_response.content)
    buffer_image.seek(0)
    response = HttpResponse(buffer_image, content_type=cloudimage_response.headers['content-type'])

    # Set cache headers
    if hasattr(settings, 'CLOUDIMAGE_CACHE_CONTROL'):
        try:
            response['Cache-Control'] = 'max-age={}'.format(int(settings.CLOUDIMAGE_CACHE_CONTROL))
        except:
            response['Cache-Control'] = settings.CLOUDIMAGE_CACHE_CONTROL

    return response
