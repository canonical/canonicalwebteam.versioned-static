from distutils.core import setup

setup(
    name='django-versioned-static',
    version='0.1',
    author='Robin',
    author_email='robin.winslow@canonical.com',
    packages=[
        'django_versioned_static',
        'django_versioned_static.templatetags'
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
