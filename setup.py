from setuptools import setup, find_packages

setup(
    name='canonicalwebteam.versioned-static',
    version='1.0.2',
    author='Canonical webteam',
    author_email='webteam+pypi@canonical.com',
    url='https://github.com/ubuntudesign/django-versioned-static-url',
    packages=find_packages(),
    description=(
        'A Django template tag for generating a URL for a static file, '
        'with a version string which will be effectively unique '
        'based on the contents of the file.'
    ),
    long_description=open('README.rst').read(),
    install_requires=[
        "Django >= 1.3",
    ],
)

