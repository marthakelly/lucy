lucy.py
============

Lucy is a static site generator written in Python.

### Why call her Lucy?
You've heard of Jekyll (Ruby) and Hyde (Python). In the Robert Louis Stevenson (Broadway) adaptation of Jekyll and Hyde, Lucy is the shared love interest of both Jekyll and Hyde.

### What is Lucy made of?
Lucy is written in Python. She uses Markdown for post/page markup, Jinja2 for templating, and bareBones for CSS preprocessing. 

### Usage

In the inner lucy directory run:

    python lucy.py << flag >> << options >>
    
The flags are:

    -i, --init
    will start a new lucy project!
    
    -po << post name >>, --post << post name >> 
    will create a new blog post
    
    -pa  << page name >>, --page  << page name >>
    will create a new page
    
    -g , --generate
    will generate all template pages into static pages ** and ** minify your css/js
    
    -gpo << post name >>, --generate_post << post name >>
    will generate a single post into a static page
    
    -gpa << page name >>, --generate_page << page name >>
    will generate a single page into a static page

    --help appended to any of these commands will bring up a help menu
    
The raw files are in the source directory, the files are generated into the deploy directory. Bootstrap your favorite deployment method :)

### In the works:
local webserver
prettier templates