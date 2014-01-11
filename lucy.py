from __future__ import absolute_import

import os
import markdown
import time
import re

FRONT_PAGE_LIMIT = 3
TEMPLATE_PATH = 'templates'
SOURCE_PATH = 'posts/'
BUILD_PATH = 'build/posts'
# lucifer
START_CHARS = '{{'
END_CHARS = '}}'

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

def build_html(post):
    """Build markdown post to HTML"""
    with open('%s/%s' % (SOURCE_PATH, post)) as f:
        return markdown.markdown(f.read())

def lucifer():
    """Templating engine for lucy"""
    # TODO: check if a file has changed before building it
    # TODO different templates
    # turn this into a class
    posts = get_markdown_posts()
    for post in posts:
        html = build_html(post)
        evaluate_template('base.html', post=html, title='test')

def evaluate_template(template_name, **kwargs):
    """Find template variables and replace them with content"""
    template = open('%s/%s' % (TEMPLATE_PATH, template_name), 'r+')
    output = ''
    for line in template:
        if any(key in line for key in kwargs.keys()):
            #TODO make not whitespace sensitive
            output += re.sub('%s( %s )%s' % (START_CHARS, key, END_CHARS), kwargs.get(key), line)

    template.close()

    with open('%s/%s.html' % (BUILD_PATH, 'hi'), 'w') as f:
        f.write(output)

def create_new_post(name):
    """Create new timestamped markdown post"""
    date = time.strftime('%m-%d-%Y')
    with open('%s%s-%s.md' % (SOURCE_PATH, name, date),  'w+'): pass

def build():
    """Build source files"""
    lucifer()
    #add_to_index()
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
