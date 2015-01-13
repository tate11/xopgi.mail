#!/usr/bin/env python
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------
# xopgi.mail.xopgi_mail._release
#----------------------------------------------------------------------
# Copyright (c) 2013, 2014 Merchise Autrement and Contributors
# All rights reserved.
#
# This is free software; you can redistribute it and/or modify it under the
# terms of the LICENCE attached (see LICENCE file) in the distribution
# package.
#


from __future__ import (division as _py3_division,
                        print_function as _py3_print,
                        unicode_literals as _py3_unicode,
                        absolute_import as _py3_abs_imports)

def read_terpfile():
    import os
    with open(os.path.join(os.path.dirname(__file__), '__openerp__.py'), 'rU') as fh:
        content = fh.read()
        return eval(content, {}, {})

_TERP = read_terpfile()
VERSION = _TERP['version']