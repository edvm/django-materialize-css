# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


setup(
    name="django-materialize-css",
    version="0.0.1",
    packages=find_packages(),
    package_data={
        'materialize': [
            'static/materialize/*.html',
            'static/materialize/bin/*.css',
            'static/materialize/bin/*.js',
            'static/materialize/css/*.css',
            'static/materialize/font/material-design-icons/*',
            'static/materialize/font/roboto/*',
            'static/materialize/images/*',
            'static/materialize/jade/*',
            'static/materialize/js/*',
            'static/materialize/js/date_picker/*',
            'static/materialize/sass/*',
        ],
    },

    # metadata for upload to PyPI
    author="Emiliano Dalla Verde Marcozzi",
    author_email="edvm@fedoraproject.org",
    description="Provides a Django app whose static folder contains Materialize CSS assets",
    license="GPL v3",
    keywords="django material design app staticfiles materialize css",
    url="https://github.com/edvm/django-materialize-css",
    download_url="http://pypi.python.org/pypi/django-materialize-css",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Libraries',
    ]
)

