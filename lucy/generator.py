from jinja2 import Environment, FileSystemLoader
from config import *
import markdown
import os

env = Environment(loader = FileSystemLoader('source/templates'))

def init():
    dirs = ['static', 'source', 'static/blog', 'static/css', 'static/img', 'static/img', 'static/js', 'source/css', 'source/img', 'source/js', 'source/posts', 'source/templates']
    for path in dirs:
        if not os.path.exists(path):
            os.makedirs(path)

def pretty():
    try:
        a = os.system('ls /utils/pretty.css > ~/source/css/style.css')
    except IOError, detail:
        print 'Cannot create Pretty template', detail
        os.exit()

def generate_file(filename):
    print 'generating page: ' + filename
    
    template = env.get_template(filename)

    # grab markdown file that needs converting
    input_file = open("source/templates/" + filename)
    text = input_file.read()

    # strip out the post meta data
    md = markdown.Markdown()

    # convert markdown file
    html = md.convert(text)

    title = filename.replace('.html', '').title()
    
    # render template context with markdown and other variables
    static_page_content = template.render(title=config['title'] + " - " + title)

    # write to the new file
    file = open('static/' + filename, 'w')
    file.write(static_page_content)
    file.close()

def generate_blog_post(post_name):
    print 'generating blog post: ' + post_name
    template = env.get_template('page-template.html');

    post = open("source/posts/" + post_name, mode="r")
    text = post.read()

    md = markdown.Markdown(extensions=['meta'])

    html = md.convert(text)
    
    title = post_name.replace('.markdown', '').title()
    
    static_page_content = template.render(blog=html, meta=md.Meta, title=title)
    
    post_url = post_name.replace('.markdown', '.html')
    
    file = open('static/blog/' + post_url, 'w')
    file.write(static_page_content)
    file.close()
    
def generate_all():
    # generate pages
    for file in os.listdir('source/templates'):
        if file == 'page-template.html':
            pass
        elif file == 'base.html':
            pass
        else:
            generate_file(file)

    # generate posts
    for file in os.listdir('source/posts'):
        generate_blog_post(file)
        
    # minify CSS
    os.system('python ../setup.py minify_css --sources /Users/marthakelly/Sites/hackerschool/lucy/lucy/source/css/style.css --output /Users/marthakelly/Sites/hackerschool/lucy/lucy/static/css/all-min.css --charset utf-8')
    
    # minify JS
    os.system('python ../setup.py minify_js --sources /Users/marthakelly/Sites/hackerschool/lucy/lucy/source/js/init.js --output /Users/marthakelly/Sites/hackerschool/lucy/lucy/static/js/all-min.js --charset utf-8')
    
def make_post(post_name):    
    markdown_header = "layout: post" + "\n" + "title: '" + post_name + "'" + "\n" + "date: 2012-05-21 18:30" + "\n" + "comments: true" + "\n" + "categories: []" + "\n"

    post_url = post_name.replace(' ', '-').lower()
    
    file = open('source/posts/' + post_url + '.markdown', 'w')
    file.write(markdown_header)
    file.close() 
    
def make_page(page_name):
    page_template = open('source/templates/page-template.html', 'r')

    html = page_template.read()

    file = open('source/templates/' + page_name + '.html', 'w')
    file.write(html)
    file.close()
