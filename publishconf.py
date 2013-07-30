#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import os, sys

sys.path.append(os.getcwd())

#If no pelicanconf_local.py then pelicanconf.py
try:
    from pelicanconf_local import *
except ImportError:
    from pelicanconf import *

SITEURL = 'http://openstack.cz'
DOMAIN = 'openstack.cz'

# Delete the content of the output directory before generating new files.
DELETE_OUTPUT_DIRECTORY = True

# Uncomment following line for absolute URLs in production:
RELATIVE_URLS = False

GOOGLE_ANALYTICS = 'UA-42741055-1'
GOOGLE_SITE_SEARCH_URL = SITEURL