# -*- coding: utf-8 -*-

AUTHOR = u'Josef Ježek'
AUTHOR_LINK = 'http://about.me/josefjezek'
SITENAME = u'OpenStack'
SITEURL = 'http://openstack.cz'
DOMAIN = 'openstack.cz'
TIMEZONE = 'Europe/Prague'
LOCALE = 'cs_CZ.UTF-8'
DEFAULT_LANG = 'cs'

# can be useful in development, but set to False when you're ready to publish
RELATIVE_URLS = True

GITHUB_URL = 'https://github.com/josefjezek/openstack.cz'
DISQUS_SITENAME = 'openstackcz'
TWITTER_USERNAME = 'openstackcz'
FACEBOOK_APPID = ''
PDF_GENERATOR = False
REVERSE_CATEGORY_ORDER = True
DEFAULT_PAGINATION = 5

FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

LINKS = (
    ('OpenStack Blog', 'http://www.openstack.org/blog/'),
    ('OpenStack Planet', 'http://planet.openstack.org/'),
)

SOCIAL = (
    ('twitter', 'http://twitter.com/openstackcz'),
    ('github', 'https://github.com/josefjezek/openstack.cz'),
)

THEME = 'themes/bootflat'
CUSTOM_CSS = 'custom.css'
META_KEYWORDS = 'openstack, cloud, linux, ubuntu, red hat'
META_DESCRIPTION = u'Česká (a slovenská) komunita kolem svobodné technologie OpenStack pro provoz cloudů typu IaaS (infrastruktura jako služba).'
GOOGLE_ANALYTICS = 'UA-42741055-1'
DISPLAY_PAGES_ON_MENU = True
GOOGLE_SITE_SEARCH_URL = SITEURL
CONTACT_MAP_LOCATION='Praha,+Czech'


# custom home page
DIRECT_TEMPLATES = (('index', 'blog', 'tags', 'categories', 'archives'))
PAGINATED_DIRECT_TEMPLATES = (('blog',))
TEMPLATE_PAGES = {
    'home.html': 'index.html',
}

# custom page generated with a jinja2 template
TEMPLATE_PAGES = {
    'contact.html': 'contact.html',
    'about.html': 'about.html',
}


OUTPUT_PATH = 'output'
PATH = 'content'

ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{slug}/index.html'

# global metadata to all the contents
# DEFAULT_METADATA = (('yeah', 'it is'),)

# static paths will be copied without parsing their contents
STATIC_PATHS = ['images',]

# list of files to copy from the source to the destination
FILES_TO_COPY = (
    ('extra/favicon.ico', 'favicon.ico'),
    ('extra/robots.txt', 'robots.txt'),
    ('extra/CNAME', 'CNAME'),
)
