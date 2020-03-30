# flake8: noqa
from django.core.exceptions import *
from django.forms import *
from django.shortcuts import *


@type.__call__
class dj:
    """Consolidated namespace for Django imports, for interactive use.

    Please don't use anything remotely resembling this class in any code
    that might ever even conceivably be shipped to production.
    """

    def __getattr__(self, name):
        """Try getting the name from the module-scope wildcard imports."""
        try:
            return globals()[name]
        except KeyError:
            raise AttributeError(name)

    from django import apps
    from django import conf
    from django import contrib
    from django import core
    from django import db
    from django import dispatch
    from django import forms
    from django import http
    from django import middleware
    from django import shortcuts
    from django import template
    from django import test
    from django import urls
    from django import utils
    from django import views
    from django.apps import AppConfig
    from django.conf import global_settings
    from django.conf import settings
    from django.contrib import admin
    from django.core import asgi
    from django.core import cache
    from django.core import checks
    from django.core import exceptions
    from django.core import files
    from django.core import handlers
    from django.core import mail
    from django.core import management
    from django.core import paginator
    from django.core import serializers
    from django.core import servers
    from django.core import signals
    from django.core import signing
    from django.core import validators
    from django.core import wsgi
    from django.db import backends
    from django.db import migrations
    from django.db import models
    from django.db import transaction
    from django.db.models import Model
    from django.forms import fields
    from django.forms import Form
    from django.shortcuts import get_list_or_404
    from django.shortcuts import get_object_or_404
    from django.shortcuts import redirect
    from django.shortcuts import render
    from django.shortcuts import resolve_url


d = j = dj
