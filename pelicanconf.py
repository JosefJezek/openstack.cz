#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys

sys.path.append(os.getcwd())
from userconf import *
from functions import *

SITEURL = 'http://localhost:8000'

TIMEZONE = 'Europe/Prague'
LOCALE = ( # http://docs.getpelican.com/en/latest/settings.html#date-format-and-locale
    'usa', 'cze',           # On Windows
    'en_US', 'cs_CZ.UTF-8', # On Unix/Linux
)
DEFAULT_LANG = 'cs'

# On Unix/Linux
DATE_FORMATS = {
    'en': ('en_US','%a, %d %b %Y'),
    'cs': ('cs_CZ.UTF-8','%a %d. %b %Y %H:%M'),
}

# On Windows
#DATE_FORMATS = {
#    'en': ('usa','%a, %d %b %Y'),
#    'cs': ('cze','%Y-%m-%d(%a)'),
#}

# Can be useful in development, but set to False when you're ready to publish.
RELATIVE_URLS = True

PDF_GENERATOR = False
REVERSE_CATEGORY_ORDER = True
DEFAULT_PAGINATION = 5
DISPLAY_PAGES_ON_MENU = True

FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

# Markdown
MD_EXTENSIONS = ['codehilite','extra']
OUTPUT_SOURCES = 'True'
OUTPUT_SOURCES_EXTENSION = '.txt'

THEME = 'themes/bootflat'
CSS_FILE = 'main.css'
CUSTOM_CSS = 'custom.css'

# Custom home page
DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives', 'blog'))
PAGINATED_DIRECT_TEMPLATES = (('blog',))

# Custom pages generated with a jinja2 template:
TEMPLATE_PAGES = {
    'pages/home.html': 'index.html',
    'pages/contact.html': 'contact.html',
    'pages/about.html': 'about.html',
}

OUTPUT_PATH = 'output'
PATH = 'content'

ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{slug}/index.html'

# Global metadata to all the contents:
# DEFAULT_METADATA = (('yeah', 'it is'),)

# Static paths will be copied without parsing their contents:
STATIC_PATHS = ['images',]

# List of files to copy from the source to the destination:
FILES_TO_COPY = (
    ('extra/favicon.ico', 'favicon.ico'),
    ('extra/robots.txt', 'robots.txt'),
    ('extra/CNAME', 'CNAME'),
)