#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# --------------------------------------------------------------------------
# xopgi_mail_forward.__openerp__
# --------------------------------------------------------------------------
# Copyright (c) 2014 Merchise Autrement and Contributors
# All rights reserved.
#
# Author: Eddy Ernesto del Valle Pino <eddy@merchise.org>
# Contributors: see CONTRIBUTORS and HISTORY file
#
# This is free software; you can redistribute it and/or modify it under the
# terms of the LICENCE attached (see LICENCE file) in the distribution
# package.


{
    'name': 'XOPGI Mail Filters',
    'version': '1.0',
    'author': 'Merchise Autrement',
    'category': 'Social Network',
    'application': False,
    'installable': True,
    'summary': 'Add default filters for messages.',
    'depends': ['base', 'mail'],
    'update_xml': [
        'views/mail_message_search.xml',
    ],
}