from jinja2 import Environment, PackageLoader
from config import *
import markdown
import codecs
import sys
import os

# func to process all files

# set up jinja and get template to render
env = Environment(loader=PackageLoader('test', 'templates'))

print config["title"]

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
    print md.Meta

    # render template context with markdown and other variables
    static_page_content = template.render(blog=html, meta=md.Meta)

    # print for my own benefit in the console
    # print static_page_content

    # write to the new file
    file = open('static/' + filename, 'w')
    file.write(static_page_content)
    file.close()

def generate_all():
    #for file in os.listdir(sys.argv[1]):
    for file in os.listdir('templates'):
       generate_file(file)
    
def make_post(post_name):
    print "making post"
    
    markdown_header = "layout: post" + "\n" + "title: '" + post_name + "'" + "\n" + "date: 2012-05-21 18:30" + "\n" + "comments: true" + "\n" + "categories: []" + "\n"
        
    file = open('posts/' + post_name + '.markdown', 'w')
    file.write(markdown_header)
    file.close() 
    
def make_page(page_name):
    print "making post"

    page_template = open('templates/page-template.html', 'r')
    html = page_template.read()
    
    file = open('templates/' + page_name + '.html', 'w')
    file.write(html)
    file.close()