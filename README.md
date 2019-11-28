# canonical-webteam.versioned-static

A `{% versioned_static %}` Django template tag for generating a URL for
a static file, with a version string which will be effectively unique
based on the contents of the file.

## Example

```
/static/css/global.css?v=a23bd10
```

## Installation

``` python
# settings.py
INSTALLED_APPS += ['django_versioned_static_url']
```

## Usage

The following template code:

``` html
{% load versioned_static %}
<link rel="stylesheet" href="{% versioned_static 'css/global.css' %}" />
```

Outputs:

``` html
<link rel="stylesheet" href="/static/css/global.css?v=feb0d0e" />
```
