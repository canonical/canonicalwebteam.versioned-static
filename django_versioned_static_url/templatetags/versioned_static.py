# System
from hashlib import sha1
from os.path import isfile

# Modules
import chardet
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

    if not full_path:
        msg = 'Could not find static file: {0}'.format(file_path)
        raise Exception(msg)

    url = static(file_path)
    versioned_url_path = url

    with open(full_path, 'r') as file_contents:
        file_data = file_contents.read()

        # # Normalise encoding
        try:
            encoding = chardet.detect(file_data)['encoding']
            file_data = file_data.decode(encoding)
        except ValueError:
            pass
        file_data = file_data.encode('utf-8')

        # 7 chars of sha1 hex
        sha1_hash = sha1(file_data)
        sha1_hex = sha1_hash.hexdigest()[:7]

        versioned_url_path += '?v=' + sha1_hex

    return versioned_url_path


register.simple_tag(versioned_static)
