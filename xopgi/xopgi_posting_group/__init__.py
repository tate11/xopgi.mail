#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# Copyright (c) Merchise Autrement [~º/~] and Contributors
# All rights reserved.
#
# This is free software; you can do what the LICENCE file allows you to.
#

from xoeuf import MAJOR_ODOO_VERSION


if MAJOR_ODOO_VERSION < 9:
    from . import no_autofollow  # noqa
