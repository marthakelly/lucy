import argparse
from generator import make_post

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--post", help="create a new blog post")
args = parser.parse_args()

if args.post:
    print (args.post)
    make_post(args.post)
else:
    print ("nope")