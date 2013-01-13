from jinja2 import Environment, FileSystemLoader
from config import *
import markdown
import os

# TODO create truncated/aggregated view of all posts on index

env = Environment(loader = FileSystemLoader("utils/templates"))

def init():
    # TODO add prompt if they want to override this directory with a new clean project
    dirs = ["static", "source", "static/blog", "static/css", "static/img", "static/img", "static/js", "source/css", "source/img", "source/js", "source/posts", "utils/templates"]
    for path in dirs:
        if not os.path.exists(path):
            os.makedirs(path)

def pretty():
    try:
        os.system("cp utils/pretty.css static/css/style.css")
    except IOError, detail:
        print "Cannot create Pretty template", detail
        os.exit()

# TODO format DATE
# TODO make_page/make_post/generate_page/generate_post could be generic and reused in two methods
def make_page(page):
    # format page header for markdown
    markdown_header = "layout: page" + "\n" + "title: "" + post + """ + "\n" + "date: 2012-05-21 18:30" + "\n" + "comments:" + config[comments_enabled]  + "\n" + "categories: []" + "\n"
    # format URL
    url = page.replace(" ", "-").lower()
    # write to file 
    file = open("source/pages/" + url + ".markdown", "w")
    file.write(markdown_header)
    file.close() 

    # print confirmation
    print "Created new page: " + page

# TODO format DATE
def make_post(post):    
    # format post header for markdown
    markdown_header = "layout: post" + "\n" + "title: "" + post + """ + "\n" + "date: 2012-05-21 18:30" + "\n" + "comments:" + config[comments_enabled] + "\n" + "categories: []" + "\n"
    # format URL
    url = post.replace(" ", "-").lower()
    # write to file 
    file = open("source/posts/" + url + ".markdown", "w")
    file.write(markdown_header)
    file.close() 
    # print confirmation
    print("Created new post: " + post)

def generate_page(page):
    # get jinja template
    template = env.get_template('page.html')
    # get markdown file that needs converting
    content = open("source/pages/" + page)
    content = file.read()
    # convert markdown file
    md = markdown.Markdown()
    html = md.convert(content)
    # format page title
    title = page.replace(".html", "").replace("-", "").title()
    # render template context with markdown and other variables
    static_page = template.render(title=config["title"] + " - " + title, content=content)
    # format page extension
    url = page.replace('markdown', 'html')
    # write generated html to new file
    file = open("static/" + url, "w")
    file.write(static_page)
    file.close()

    # print confirmation
    print "Generated page: " + page 

def generate_post(post):
    # get jinja template
    template = env.get_template('page.html')
    # get markdown file that needs converting
    content = open("source/posts/" + post)
    content = file.read()
    # convert markdown file
    md = markdown.Markdown()
    html = md.convert(content)
    # format page title
    title = post.replace(".html", "").replace("-", "").title()
    # render template context with markdown and other variables
    static_page = template.render(title=config["title"] + " - " + title, content=content)
    # write generated html to new file
    file = open("static/" + filename, "w")
    file.write(static_page)
    file.close()

    # print confirmation
    print "Generated post: " + post
    
# generate all pages and posts into static assets
# minify css/js
def generate_all():
    # generate pages
    for page in os.listdir("source/pages"):
        generate_page(page)
    # generate posts
    for file in os.listdir("source/posts"):
        generate_post(file)
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
    # minify CSS
    # TODO fix the paths for minify
    os.system("python ../setup.py minify_css --sources /Users/marthakelly/Sites/hackerschool/lucy/lucy/source/css/style.css --output /Users/marthakelly/Sites/hackerschool/lucy/lucy/static/css/all-min.css --charset utf-8")
    # minify JS
    os.system("python ../setup.py minify_js --sources /Users/marthakelly/Sites/hackerschool/lucy/lucy/source/js/init.js --output /Users/marthakelly/Sites/hackerschool/lucy/lucy/static/js/all-min.js --charset utf-8")
