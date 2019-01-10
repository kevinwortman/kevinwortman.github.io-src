#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# local-dev versus public-web
#SITEURL = ''
SITEURL = 'https://kevinwortman.com'

THEME = 'Flex'
AUTHOR = 'Kevin A. Wortman'
SITENAME = "Kevin Wortman's Homepage"
SITETITLE = SITENAME
SITELOGO = SITEURL + '/pages/profile2019.jpg'
COPYRIGHT_YEAR = 2019

PATH = 'content'
TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = 'en'

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MAIN_MENU = True

SOCIAL = (('github', 'https://github.com/kevinwortman/'),
          ('linkedin', 'https://www.linkedin.com/in/kevin-wortman-38a69a23/'),
          ('quora', 'https://www.quora.com/profile/Kevin-Wortman'),
          ('envelope', 'mailto:kwortman@fullerton.edu'),
          ('rss', SITEURL + '/' + FEED_ALL_ATOM),)

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
