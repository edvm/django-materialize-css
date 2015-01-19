Overview
========

This package provides a `Django <https://www.djangoproject.com>`_ app whose static folder contains
the sources of `Materialize CSS <http://materializecss.com>`_, nothing more and nothing
less. `Materialize` is a modern responsive front-end framework based on `Material Design` (created
by Google).
The un-minified scss and javascript sources are included to be
integrated into your Django site as you see fit. If you simply want to use the minified CSS and JS
files provided by the Materialize project, you probably don't need this anyway.

And that's it! Materialize pre-packaged for Django.

Setup
=====

First, install the app::

    pip install django-materialize-css

Then include it in your Django project::

    # settings.py:

    INSTALLED_APPS = (
        ...
        'materialize',
        ...
    )

This also assumes you haven't removed ``django.contrib.staticfiles.finders.AppDirectoriesFinder``
from the ``STATICFILES_FINDERS`` config setting.

