from jinja2 import Environment, FileSystemLoader
from config import *
import markdown
import os

env = Environment(loader = FileSystemLoader('lucy/templates'))

def generate_file(filename):
    template = env.get_template(filename)

    # grab markdown file that needs converting
    input_file = open("lucy/templates/" + filename)
    text = input_file.read()

    # strip out the post meta data
    md = markdown.Markdown()

    # convert markdown file
    #html = md.convert(text)

    title = filename.replace('.html', '').title()
    print title
    
    # render template context with markdown and other variables
    static_page_content = template.render(title=config['title'] + " - " + title)

    # write to the new file
    file = open('build/' + filename, 'w')
    file.write(static_page_content)
    file.close()

def generate_blog_post(post_name):
    template = env.get_template('page-template.html');
        
    post = open("lucy/posts/" + post_name, mode="r")
    text = post.read()

    md = markdown.Markdown(extensions=['meta'])

    html = md.convert(text)
    
    title = post_name.replace('.markdown', '').title()
    
    static_page_content = template.render(blog=html, meta=md.Meta, title=title)
    
    post_url = post_name.replace('.markdown', '.html')
    
    file = open('build/blog/' + post_url, 'w')
    file.write(static_page_content)
    file.close()
    
def generate_all():
    # generate pages
    for file in os.listdir('lucy/templates'):
        if file == 'page-template.html':
            pass
        elif file == 'base.html':
            pass
        else:
            generate_file(file)

    # generate posts
    for file in os.listdir('lucy/posts'):
        generate_blog_post(file)
        
    # generate CSS from bareBones  
    os.system('node lucy/js/bareBones.js lucy/css/main.bare')
    
    # minify CSS
    os.system('python setup.py minify_css --sources lucy/css/*.css --output build/css/all-min.css')
    
    # minify CSS as separate files
    #os.system('python setup.py minify_css --sources lucy/css/*.css --output build/css/%s-min.css')
    
    # minify JS
    os.system('python setup.py minify_js --sources lucy/js/*.js --output build/js/all-min.js')
    
    # minify JS as separate files
    # os.system('python setup.py minify_js --sources lucy/js/*.js --output build/js/%s-min.js')
    
def make_post(post_name):
    print "making post"
    
    markdown_header = "layout: post" + "\n" + "title: '" + post_name + "'" + "\n" + "date: 2012-05-21 18:30" + "\n" + "comments: true" + "\n" + "categories: []" + "\n"

    post_url = post_name.replace(' ', '-').lower()
    
    file = open('lucy/posts/' + post_url + '.markdown', 'w')
    file.write(markdown_header)
    file.close() 
    
def make_page(page_name):
    print "making page"

    page_template = open('page-template.html', 'r')

    html = page_template.read()

    file = open('templates/' + page_name + '.html', 'w')
    file.write(html)
    file.close()