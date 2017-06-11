# System
from hashlib import md5

# Modules
import logging
from django import template
from django.contrib.staticfiles.finders import find
from django.templatetags.static import static


logger = logging.getLogger(__name__)

register = template.Library()


def versioned_static(file_path):
    """
    Given the path for a static file
    Output a url path with a hex has query string for versioning
    """

    full_path = find(file_path)
    url = static(file_path)

    if type(full_path) is list and len(full_path) > 0:
        full_path = full_path[0]

    if not full_path:
        msg = 'Could not find static file: {0}'.format(file_path)
        logger.warning(msg)
        return url

    # Use MD5 as we care about speed a lot
    # and not security in this case
    file_hash = md5()
    with open(full_path, "rb") as file_contents:
        for chunk in iter(lambda: file_contents.read(4096), b""):
            file_hash.update(chunk)

    return url + '?v=' + file_hash.hexdigest()[:7]


register.simple_tag(versioned_static)
