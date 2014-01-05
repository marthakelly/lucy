from __future__ import absolute_import

import os
import markdown
import time

FRONT_PAGE_LIMIT = 3
SOURCE_PATH = 'posts/'
BUILD_PATH = 'build/posts'

def get_markdown_posts():
    """Return source posts"""
    return os.listdir(SOURCE_PATH)

def get_html_posts():
    """Return built posts"""
    return os.listdir(BUILD_PATH)

def add_to_index():
    """Add recent posts to index.html"""
    posts = get_html_posts()
    for post in posts[:FRONT_PAGE_LIMIT]:
        pass

def add_to_archive(link):
    """Add links to archived posts to archives.html"""
    posts = get_html_posts()
    for post in posts[FRONT_PAGE_LIMIT:]:
        pass

def build_posts():
    """Build source posts to HTML"""
    # TODO: check if a file has changed before building it
    posts = get_markdown_posts()
    for post in posts:
        print '=^..^= building %s' % post
        markdown.markdownFromFile(
                input='%s/%s' % (SOURCE_PATH, post),
                output='%s/%s' % (BUILD_PATH, post))

def create_new_post(name):
    """Create new timestamped markdown post"""
    date = time.strftime("%m-%d-%Y")
    with open('%s%s-%s.md' % (SOURCE_PATH, name, date),  'w+'): pass

def build():
    """Build source files"""
    build_posts()
    add_to_index()
    #add_to_archive()

def deploy():
    """Deploy application to github pages"""
    pass

# add argv
build()
# add argv
# deploy()
# add argv
# create_new_post()
