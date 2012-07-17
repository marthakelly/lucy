from jinja2 import Environment, PackageLoader
import markdown
import codecs

env = Environment(loader=PackageLoader('test', 'templates'))
template = env.get_template('index.html')


#md = markdown.Markdown()
#post = md.convertFile(input="posts/first-post.markdown", output="static/first-post.html", encoding="utf8")
#post = md.convert("posts/first-post.markdown")

input_file = codecs.open("posts/first-post.markdown", mode="r", encoding="utf-8")
text = input_file.read()
html = markdown.markdown(text)

static_page_content = template.render(the='variables', go='here', blog=html)

print static_page_content

file = open('static/index.html', 'w')
file.write(static_page_content)
file.close()

