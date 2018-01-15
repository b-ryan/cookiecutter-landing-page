#!/usr/bin/env python
import time

AUTHOR = "Buck Ryan"
SITENAME = "{{cookiecutter.sitename}}"
TAGLINE = "{{cookiecutter.tagline}}"
TIMEZONE = "America/New_York"
DEFAULT_LANG = "en"
TEMPLATE_PAGES = {
    # eg: "pricing.html": "pricing.html",
}
# The following disables the ordinary generation of pages that are meant for
# blogs
ARCHIVES_SAVE_AS = ""
ARCHIVE_SAVE_AS = ""
AUTHORS_SAVE_AS = ""
AUTHOR_SAVE_AS = ""
CATEGORIES_SAVE_AS = ""
CATEGORIE_SAVE_AS = ""
TAGS_SAVE_AS = ""
TAG_SAVE_AS = ""
# PATH_METADATA= '(?P<dirname>.*)/(?P<basename>.*)\..*'
# PAGE_SAVE_AS= '{dirname}/{basename}.html'
# PAGE_URL= '{dirname}/{basename}.html'
THEME = "theme"
HIDE_TAGS = True
HIDE_CATEGORY = True
HIDE_AUTHORS = True
PLUGINS = ["asset_functions"]
CACHE_BUST = str(time.time())
NAV_ITEMS = [
    {
        "text": "Home",
        "file": "index.html",
        "link": "/",
    }
]
