import argparse
from generator import make_post, make_page, generate_all, generate_blog_post, generate_file

parser = argparse.ArgumentParser()
parser.add_argument("-po", "--post", help="Create a new blog post")
parser.add_argument("-pa", "--page", help="Create a new page")
parser.add_argument("-g", "--generate", help="Generate all posts and template pages into static pages",
                    action="store_true")
parser.add_argument("-gpo", "--generate_post", help="Turn an individual Markdown page into a HTML blog post page")
parser.add_argument("-gpa", "--generate_page", help="Turn an individual Jinja template into a static HTML page")
parser.add_argument("-i", "--init", help="Start a new Lucy project!")
# parser.add_argument("-pr", "--preview", help="Initialize Lucy with a pretty template.")
# parser.add_argument("-d", "--deploy", help="Initialize Lucy with a pretty template.")
# parser.add_argument("-p", "--pretty", help="Initialize Lucy with a pretty template.")
# parser.add_argument("-pl", "--plain", help="Initialize Lucy with a plain template.")

args = parser.parse_args()

if args.post:
    make_post(args.post)
elif args.page:
    make_page(args.page)
elif args.generate:
    generate_all()
elif args.generate_post:
    generate_blog_post(args.generate_post)
elif args.generate_page:
    generate_file(args.generate_page)
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