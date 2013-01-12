from setuptools import setup

VERSION = __import__(PACKAGE).__version__

setup(
    name = "lucy",
    version = VERSION,
    author = "Martha Kelly",
    author_email = "mk.girdler@gmail.com",
    description = ("Pretty, simple static site generator and blog for github pages."),
    license = "BSD",
    url = "https://www.github.com/marthakelly/lucy",
    install_requires = [
        'Markdown >= 2.0',
        'Jinja2 >= 2.5',
        'minify'
    ],
    packages = find_packages(exclude=["tests.*", "tests"]),
    package_data = find_package_data("lucy", only_in_packages=False),
    # TODO
    # long_description=read('README.md'),
    classifiers = [
        "Development Status :: 2 - Pre-Alpha",
	"Environment :: Web Environment",
	"Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
	"Operating System :: OS Independent",
        "Programming Language :: Python",
	"Framework :: Jinja2",
        "Topic :: Utilities",
    ],
    zip_safe = False,
)
