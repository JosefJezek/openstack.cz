#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Custom functions available to all templates:
from operator import itemgetter
import re

def sort_tags_by_length(tags):
    return sorted(tags, key=lambda tup: len(tup[1]), reverse=True)

def media_url(url, site_root):
    if re.match('^https?://', url, re.IGNORECASE):
        return url
    else:
        return '%s/static/images/%s' %(site_root, url)


JINJA_FILTERS = {
    'sort_tags_by_length': sort_tags_by_length,
    'media_url': media_url,
}