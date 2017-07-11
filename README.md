# django-cloudimage

A Django wrapper for https://cloudimage.io

## Installation

Install via pip:

```
pip install django-cloudimage
```

## Usage

1. Add to `INSTALLED_APPS` in `settings.py` `'cloudimage',`
2. Add the `CLOUDIMAGE_TOKEN` in `settings.py`
2. Add the include to urlpatterns in `urls.py`
   ```
   urlpatterns = [ url(r'^media/', include('cloudimage.urls')), ]
   ```
3. Load the template tag into a template `{% load cloudimage %}`
4. Use the `image` tag. `{% image 'path/to/image.jpg' width=100 %}`
   Visit the [CloudImage Docs](https://cloudimage.io/en/docs/introduction) for all of the options.
   Convert parameters to kwargs.

## Options

### Cache Control headers

It is highly recommended that if you use this package your site should be sitting behind a CDN. Not sure what this is, check out https://www.cloudflare.com/

Add to `settings.py`

To set an expiration timeout use an integer in seconds. For example, below the image is set to cache for an hour.

```
CLOUDIMAGE_CACHE_CONTROL = 3600
```
This will output `Cache-Control max-age=3600` in the response header.

**The advanced option**

Any string you pass that doesn't convert to an int will be set in the header.

```
CLOUDIMAGE_CACHE_CONTROL = "no-cache"
```
This will output `Cache-Control no-cache` in the response header.

## Caveats

* [KISS](https://en.wikipedia.org/wiki/KISS_principle)
* The origional image must be accessable via a URL, so RSZ.IO can access it. I use [django-storages](https://django-storages.readthedocs.io/en/latest/) with AWS S3 to serve my media.
* This is tested and used in production with Django 1.10 and 1.11 on Python 3.5 and 3.6. But this should work on older versions of Django and Python 2. Open an issue or pull request if not the case.

## Versioning
The package is following the Major.Minor.BugFix philosophy. So breaking changes will increase the major number. New features will increase the minor number.

So it is safe to put this line in your `requirements.txt`

**All new features, no breaking features**

```
django-cloudimage>=1.0.0,<2.0
```

**Just bugfixes**

```
django-cloudimage>=1.0.0,<1.1
```

## Release Notes

This project is using GitHub's release feature. Find the release notes here [https://github.com/g3rd/django-cloudimage/releases](https://github.com/g3rd/django-cloudimage/releases)
