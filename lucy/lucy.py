import argparse
from generator import *

parser = argparse.ArgumentParser()

parser.add_argument("-i", "--init", help="Start a new Lucy project!")
parser.add_argument("-po", "--post", help="Create a new markdown blog post")
parser.add_argument("-pa", "--page", help="Create a new markdown page")
parser.add_argument("-g", "--generate", help="Generate all posts and template pages into static pages",
                    action="store_true")
parser.add_argument("-gpo", "--generate_post", help="Turn an individual Markdown page into a static HTML blog post")
parser.add_argument("-gpa", "--generate_page", help="Turn an individual Jinja template into a static HTML page")
# parser.add_argument("-pr", "--preview", help="Initialize Lucy with a pretty template.")
# parser.add_argument("-d", "--deploy", help="Initialize Lucy with a pretty template.")
# parser.add_argument("-p", "--pretty", help="Initialize Lucy with a pretty template.")
# parser.add_argument("-pl", "--plain", help="Initialize Lucy with a plain template.")

args = parser.parse_args()

if args.init:
    pass
elif args.post:
    make_new('post', args.post)
elif args.page:
    make_new('page', args.page)
elif args.generate:
    generate_all()
elif args.generate_post:
    make_static('post', args.generate_post)
elif args.generate_page:
    make_static('page', args.generate_page)
else:
    print ("nope")
    
##### TODO ####
# minify CSS/JS
# deploy to gihub pages
# pretty template
# set up default lucy directories correctly
# set up local dev server
# add more functionality to bareBones and put it in NPM
# put this in pypi
# document the shit out of it
