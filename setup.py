import os
from setuptools import setup

setup(
    name = "lucy",
    version = "0.0.1",
    author = "Martha Kelly",
    author_email = "mk.girdler@gmail.com",
    description = ("Pretty, simple static site generator."),
    license = "BSD",
    keywords = "lucy static site generator jinja2 markdown blog responsive",
    url = "https://www.github.com/marthakelly/lucy",
    install_requires = [
        'Markdown >= 2.0',
        'Jinja2 >= 2.5',
        'minify'
    ],
    packages = find_packages(),
    # TODO
    # long_description=read('README.md'),
    classifiers = [
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: BSD License",
        'Programming Language :: Python',
        "Topic :: Utilities"
    ],
)
