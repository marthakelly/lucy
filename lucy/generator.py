from jinja2 import Environment, FileSystemLoader
from config import *
import markdown
import os

# TODO create check to see if existing pages have changed or not??
# WATCHDOG
env = Environment(loader = FileSystemLoader("lucy/utils/templates"))
posts = []

def init():
    # TODO add prompt if they want to override this directory with a new clean project
    dirs = ["static", "source", "static/posts", "static/css", "static/img", "static/img", 
        "static/js", "source/css", "source/img", "source/js", "source/posts", "utils/templates"]

    for path in dirs:
        if not os.path.exists(path):
            os.makedirs(path)

def pretty():
    try:
        os.system("cp utils/pretty.css static/css/style.css")
    except IOError, detail:
        print "Cannot create template: ", detail
        os.exit()

# TODO format DATE
def make_new(item, title):
    # format url
    directory = "lucy/source/" + item + "s/"
    name = title.replace(" ", "-").lower() + ".markdown"
    url = config["base_url"] + "/posts/" + name.replace(".markdown", ".html")
    # format page header for markdown
    markdown_header = "layout: " + item + "\n" + "title: " + title + "\n" + "date: 2012-05-21 18:30" + "\n" + "comments: " + config["comments_enabled"]  + "\n" + "categories: []" + "\n" + "link: " + url
    # write to file 
    file = open(directory + name, "w")
    file.write(markdown_header)
    file.close() 

    # print confirmation
    print "Created new " + item + " - " + name

def make_static(item, title):
    # get jinja template
    template = env.get_template(item + ".html")
    # get markdown file
    content = open("lucy/source/" + item + "s/" + title, mode="r")
    text = content.read()
    # convert markdown file
    md = markdown.Markdown(extensions = ['meta'])
    html = md.convert(text)
    # format page title
    name = title.replace(".markdown", "")
    # render template context with markdown and other variables
    static_item = template.render(title=config["title"] + " - " + name, meta=md.Meta, content=html)
    # format page extension
    url = title.replace('markdown', 'html').replace(" ", "-")
    # write generated html to new file
    if item == "post":
        # add to global posts obj
        post_object = {
            'meta': md.Meta,
            'content': html
        }
        posts.append(post_object)
        path = "lucy/static/posts/"
    elif item == "page":
        path = "lucy/static/"
    # write static file
    file = open(path + url, "w")
    file.write(static_item)
    file.close()
    
    # print confirmation
    print "Generated " + item + " - " + url

# TODO make both of these more generic
def generate_index(posts):
    template = env.get_template('index.html')
    static_page = template.render(title=config["title"], posts=posts)
    # write generated html to new file
    file = open("lucy/static/index.html", "w")
    file.write(static_page)
    file.close()
    
def generate_archives():
    template = env.get_template('archives.html')
    static_page = template.render(title=config["title"] + " - archives", posts=posts)
    # write generated html to new file
    file = open("lucy/static/archives.html", "w")
    file.write(static_page)
    file.close()
    
def generate_rss(posts):
    template = env.get_template('posts.rss')
    static_page = template.render(posts=posts)
    # write generated rss to new file
    file = open("lucy/static/posts.rss", "w")
    file.write(static_page)
    file.close()

# generate all pages and posts into static assets
# create index.html
# create archives.html
# minify css/js
def generate_all():
    # generate static pages
    for page in os.listdir("lucy/source/pages"):
        if page.endswith(".markdown"):
            make_static('page', page)
    # generate static posts
    for post in os.listdir("lucy/source/posts"):
        if post.endswith(".markdown"):
            make_static('post', post)
	# create index.html
	generate_index(posts)
	generate_rss(posts)
	# create archives.html
	# generate_archives()
    # minify CSS
    # TODO fix the paths for minify
    os.system("python ../setup.py minify_css --sources /Users/marthakelly/Sites/hackerschool/lucy/lucy/source/css/style.css --output /Users/marthakelly/Sites/hackerschool/lucy/lucy/static/css/all-min.css --charset utf-8")
    # minify JS
    os.system("python ../setup.py minify_js --sources /Users/marthakelly/Sites/hackerschool/lucy/lucy/source/js/init.js --output /Users/marthakelly/Sites/hackerschool/lucy/lucy/static/js/all-min.js --charset utf-8")

'''
def generate_images():
    # check if existing images have changed
    # TODO does this work?
    for file in os.listdir("source/img"):
        try:
            with open(file) as new_img:
	            with open('static/img' + file) as old_img:
	                if new_img.read() == old_img.read():
		                pass
	                else:
		                os.system("cp" + file + "static/img/" + file)
                    except IOError:
	                    # copy over new images
                        os.system("cp " + file + " static/img/" + file)

#TODO no icky XML, use JSON
def generate_rss():
    pass
    # RSS env.get_template("feedtemplate.xml").render(items=get_list_of_items())
'''