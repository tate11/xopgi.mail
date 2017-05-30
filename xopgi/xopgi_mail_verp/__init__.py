#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# --------------------------------------------------------------------------
# xopgi_mail_verp
# --------------------------------------------------------------------------
# Copyright (c) 2015-2017 Merchise Autrement [~º/~] and Contributors
# All rights reserved.
#
# Author: Merchise Autrement [~º/~]
# Contributors: see CONTRIBUTORS and HISTORY file
#
# This is free software; you can redistribute it and/or modify it under the
# terms of the LICENCE attached (see LICENCE file) in the distribution
# package.

from __future__ import absolute_import as _py3_abs_imports

try:
    from openerp.release import version_info as ODOO_VERSION_INFO
except ImportError:
    from odoo.release import version_info as ODOO_VERSION_INFO

if (8, 0) <= ODOO_VERSION_INFO < (11, 0):
    # MIGRATION POLICY: All addons are not included until someone work on them
    # and upgrade them.

    from . import coordinated  # noqa
    from . import mail_mail  # noqa
    from . import mail_bounce_model  # noqa
