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

def build_post(post):
    """Build markdown post to HTML"""
    with open('%s/%s' % (SOURCE_PATH, post)) as f:
        return markdown.markdown(f.read())

def build_from_template(post):
    html = build_post(post)
    context = {
        'post': html
    }
    evaluate_template('base.html', context=context)

def lucifer():
    """Templating engine for lucy"""
    # TODO: check if a file has changed before building it
    # TODO different templates
    # turn this into a class
    posts = get_markdown_posts()
    for post in posts:
        build_from_template(post)
        # build_index(post)
        # build_archive(post)

def evaluate_template(template_name, **kwargs):
    """Find template variables and replace them with content"""
    context = kwargs['context']

    # do with here
    template = open('%s/%s' % (TEMPLATE_PATH, template_name), 'r+')

    output = ''

    for line in template:
        for key in context.keys():
            if key in line:
                # TODO make not whitespace sensitive
                line = re.sub('%s( %s )%s' % (START_CHARS, key, END_CHARS), context[key], line)
                print line
            output += line
    
    template.close()

    result = open('%s/%s' % (BUILD_PATH, template_name), 'w+')
    result.write(output)
    result.close()

def create_new_post(name):
    """Create new timestamped markdown post"""
    date = time.strftime('%m-%d-%Y')
    with open('%s%s-%s.md' % (SOURCE_PATH, name, date),  'w+'): pass

def build():
    """Build source files"""
    lucifer()

def deploy():
    """Deploy application to github pages"""
    pass

# add argv
build()
# add argv
# deploy()
# add argv
# create_new_post()
