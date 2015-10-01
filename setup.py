from setuptools import setup

setup(
    name='django-versioned-static-url',
    version='0.2',
    author='Robin',
    author_email='robin.winslow@canonical.com',
    url='https://github.com/ubuntudesign/django-versioned-static-url',
    packages=[
        'django_versioned_static_url',
        'django_versioned_static_url.templatetags'
    ],
    description=(
        'A template tag for generating a URL for a static file, '
        'with a version string which will be effectively unique '
        'based on the contents of the file.'
    ),
    long_description=open('README.rst').read(),
    install_requires=[
        "Django >= 1.3",
    ],
)
