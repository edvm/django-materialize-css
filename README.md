This repo is Deprecated
=======================
Please dont use me, i no longer have maintenance. But do not despair, you can go and use:
http://forms.viewflow.io/ 

Which seems to have:
 * Nice documentation
 * Maintenance
 
Thank you! 

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

Finally include the css/js directives in your html document::

    {% load staticfiles %}
    <html>
      <head>
        <!--Import materialize.css-->
        <link type="text/css" rel="stylesheet" href="{% static 'materialize/bin/materialize.css' %}"  media="screen,projection"/>
      </head>
      <body>
        ...
        <!--Import jQuery before materialize.js-->
        {% block footer %}
            <script type="text/javascript" src="https://code.jquery.com/jquery-2.1.1.min.js"></script>
            <script type="text/javascript" src="{% static 'materialize/bin/materialize.js' %}"></script>
        {% endblock %}
        ...
      </body>
    </html>

That's all!

This also assumes you haven't removed ``django.contrib.staticfiles.finders.AppDirectoriesFinder``
from the ``STATICFILES_FINDERS`` config setting.

