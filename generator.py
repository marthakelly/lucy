from jinja2 import Environment, PackageLoader
import markdown
import codecs

# set up jinja and get template to render
env = Environment(loader=PackageLoader('test', 'templates'))
template = env.get_template('index.html')

# generate html from markdown
input_file = codecs.open("posts/first-post.markdown", mode="r", encoding="utf-8")
text = input_file.read()

md = markdown.Markdown(extensions=['meta'])

html = md.convert(text)

# render template context with markdown and other variables
static_page_content = template.render(the='variables', go='here', blog=html, meta=md.Meta)

# print for my own benefit in the console
print static_page_content

# write to the new file
file = open('static/index.html', 'w')
file.write(static_page_content)
file.close()

