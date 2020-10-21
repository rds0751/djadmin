#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings

DJADMIN_DYNAMIC_FIELD_DISPLAY = getattr(settings, 'DJADMIN_DYNAMIC_FIELD_DISPLAY', True)

ADMIN_COLOR_THEME = getattr(settings, 'ADMIN_COLOR_THEME', 'blue')

ALLOW_FORGET_PASSWORD_ADMIN = getattr(settings, 'ALLOW_FORGET_PASSWORD_ADMIN', True)

ADMIN_HEADER_TITLE = getattr(settings, 'ADMIN_HEADER_TITLE', 'JR Admin')

DJADMIN_DYNAMIC_DELETE_UNREGISTER_FIELD = getattr(settings, 'DJADMIN_DYNAMIC_DELETE_UNREGISTER_FIELD', False)

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'users.User')

DJADMIN_FIELD_DEPTH = getattr(settings, 'DJADMIN_FIELD_DEPTH', 1)

DJADMIN_CONFIG_PAGE = getattr(settings, 'DJADMIN_CONFIG_PAGE', True)

DJADMIN_MANAGE_FILE_NAME = getattr(settings, 'DJADMIN_MANAGE_FILE_NAME', 'manage.py')

ALLOW_STAFF_USER_AS_VISITOR = getattr(settings, 'DJADMIN_ALLOW_STAFF_USER_AS_VISITOR', True)
