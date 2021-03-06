#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# Copyright (c) Merchise Autrement [~º/~] and Contributors
# All rights reserved.
#
# This is free software; you can do what the LICENCE file allows you to.
#

'''Disallow receiving direct mail.

.. warning:: We recommend to explicitly bounce direct mail, this module DOES
   NOT do that.

'''

from __future__ import (division as _py3_division,
                        print_function as _py3_print,
                        absolute_import as _py3_abs_import)

from xoeuf.odoo.addons.xopgi_mail_threads.routers import MailRouter


MODEL_INDEX = 0
DIRECT_MAIL_MODEL = 'res.users'


class NoDirectMailRouter(MailRouter):
    @classmethod
    def query(cls, obj, message):
        return True

    @classmethod
    def apply(cls, obj, routes, message, data=None):
        routes[:] = [
            route
            for route in routes
            if route[MODEL_INDEX] != DIRECT_MAIL_MODEL
        ]
        return routes
