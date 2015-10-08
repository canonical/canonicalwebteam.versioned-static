# System
from hashlib import sha1
from os.path import isfile

from django import template
from django.contrib.staticfiles.finders import find
from django.templatetags.static import static
from django.http import Http404


register = template.Library()


def versioned_static(file_path):
    """
    Given the path for a static file
    Output a url path with a hex has query string for versioning
    """

    full_path = find(file_path)
    url = static(file_path)

    if full_path:
        if not isfile(full_path):
            raise Http404('Static file not found')
        with open(full_path) as file_contents:
            # 7 chars of sha1 hex
            sha1_hash = sha1(file_contents.read().encode('utf-8'))
            sha1_hex = sha1_hash.hexdigest()[:7]

    versioned_url_path = url + '?v=' + sha1_hex

    return versioned_url_path


register.simple_tag(versioned_static)
