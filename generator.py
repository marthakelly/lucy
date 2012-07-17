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

def generate_all(filename):
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

#for file in os.listdir(sys.argv[1]):
#   generate_all(file
    
def make_post(post_name):
    print "making post"
    
    markdown_header = "layout: post" + "\n" + "title: '" + post_name + "'" + "\n" + "date: 2012-05-21 18:30" + "\n" + "comments: true, categories: []"
        
    file = open('posts/' + post_name + '.markdown', 'w')
    file.write(markdown_header)
    file.close() 