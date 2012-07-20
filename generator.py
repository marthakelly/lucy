from jinja2 import Environment, PackageLoader
from config import *
import markdown
#import codecs
import os

env = Environment(loader=PackageLoader('test', 'templates'))

def generate_file(filename):
    template = env.get_template(filename)

    # grab markdown file that needs converting
    input_file = codecs.open("posts/first-post.markdown", mode="r", encoding="utf-8")
    text = input_file.read()

    # strip out the post meta data
    md = markdown.Markdown(extensions=['meta'])

    # convert markdown file
    html = md.convert(text)

    # print for my benefit
    # print md.Meta

    # render template context with markdown and other variables
    static_page_content = template.render(blog=html, meta=md.Meta)

    # print for my own benefit in the console
    # print static_page_content

    # write to the new file
    file = open('build/' + filename, 'w')
    file.write(static_page_content)
    file.close()

def generate_blog_post(post_name):
    template = env.get_template('page-template.html');
        
    post = open("posts/" + post_name, mode="r")
    text = post.read()

    md = markdown.Markdown(extensions=['meta'])

    html = md.convert(text)
    
    static_page_content = template.render(blog=html, meta=md.Meta)
    
    post_url = post_name.replace('.markdown', '.html')
    
    file = open('build/blog/' + post_url, 'w')
    file.write(static_page_content)
    file.close()
    
def generate_all():
    for file in os.listdir('templates'):
        if file == 'page-template.html':
            continue
        else:
            generate_file(file)
    
    for file in os.listdir('posts'):
        print 'hai'

def make_post(post_name):
    print "making post"
    
    markdown_header = "layout: post" + "\n" + "title: '" + post_name + "'" + "\n" + "date: 2012-05-21 18:30" + "\n" + "comments: true" + "\n" + "categories: []" + "\n"
    
    post_url = post_name.replace(' ', '-').lower()
    
    file = open('posts/' + post_url + '.markdown', 'w')
    file.write(markdown_header)
    file.close() 
    
def make_page(page_name):
    print "making post"

    page_template = open('templates/page-template.html', 'r')
    html = page_template.read()
    
    file = open('templates/' + page_name + '.html', 'w')
    file.write(html)
    file.close()