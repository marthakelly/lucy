import argparse
from generator import make_post, make_page, generate_all, generate_blog_post

parser = argparse.ArgumentParser()
parser.add_argument("-po", "--post", help="create a new blog post")
parser.add_argument("-pa", "--page", help="create a new page")
parser.add_argument("-g", "--generate", help="generate all template pages into static pages",
                    action="store_true")
parser.add_argument("-gp", "--generate_post", help="turn a markdown page into a blog post page")

args = parser.parse_args()

if args.post:
    print (args.post)
    make_post(args.post)
elif args.page:
    print (args.page)
    make_page(args.page)
elif args.generate:
    print (args.generate)
    generate_all()
elif args.generate_post:
    print (args.generate_post)
    generate_blog_post(args.generate_post)
else:
    print ("nope")