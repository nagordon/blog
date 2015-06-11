Title: My First Blog [Updated]
Date: 2015-02-25
Modified: 2015-04-14
Category: Tutorials
Tags: tutorial, python, pelican
Slug: my-first-blog
Authors: Neal Gordon
Summary: How the heck I built a blog


My first whimsical thought of creating a blog was, how hard can it be? Well, as it turns out, I found it it is harder than expected. But, here it is, and here I am. This is a rough outline to how I got my blog working and how I update. I started with a github page using jekyll, but decided that I really would like ipython notebook support, so that left me with [Nickola](http://getnikola.com/) or [Pelican](http://docs.getpelican.com/en/3.5.0/#). I thought the Pelican documentation looked easier, so I went with it

## setup
I am running a windows 8 laptop with a  [Linux-Mint](http://www.linuxmint.com/) virtual machine using [VirtualBox ](https://www.virtualbox.org/)

Once your virtual machine is running, open a terminal and run the following commands in bash


install [miniconda](http://conda.pydata.org/miniconda.html) distro of python. Great package management

```bash
# updates
sudo apt-get update && sudo apt-get upgrade

# create a virtual environment 'pylican'
conda create -n pylican python=2.7
source activate pylican  # or just 'activate pylican' in windows
conda install pip
conda install ipython-notebook
pip install pelican
pip install Markdown
conda install ipython==2.4.1   # this is important because of liquid tags

# for github blogs, this tool makes it very easy to update the blog
pip install ghp-import
```

Now we need a github account and create a website [repository](https://github.com/nagordon/nagordon.github.io)

in the bash terminal, clone the github repository to your local computer 
```bash
git clone https://github.com/nagordon/nagordon.github.io.git
```

this will create a directory ```nagordon.github.io``` that will have all the website content

# notes on my blog site
when I want to add a page, create a file in the content directory

/content/new_blog_post.md

Each file should start like this.
```
Title: MyFirstReview
Date: 2010-12-03
Modified: 2010-12-05
Category: Python
Tags: pelican, publishing
Slug: my-super-post
Authors: neal gordon
Summary: short summary

This is the content of my super blog post.

```
The tags will automatically create groups at the top of your webpage once it is built

Once you have your *.md, we need to generate the static html files that will be the blog -s 
```bash
# if any troubles arise
pelican --help
# generates the site
pelican content

# or specify the config file
pelican content -s pelicanconf.py

# or to generate and preview the site
cd output
# or a simple python webserver
python -m SimpleHTTPServer

# a really handy tool to tweaking the look of your page to constantly update
make devserver

# and to stop
./develop_server.sh stop

# finally, if you did not receive any errors, push your freshly made blog to your github account, get a cup of coffee, and a few minutes later your updates should be live on the web
make github
# enter github credentials
```

## Next Steps
One of the things I really like about pelican is I can embed [ipython notebooks](http://nbviewer.ipython.org/) into the blog post. To do so, just check out this [plugin](https://github.com/danielfrg/pelican-ipynb)

**Update**
I have been using the ipynb plugin for a bit now, and it is really slick, but it doesn't render well with the CSS files, so I have switched to [liquid tags](https://github.com/getpelican/pelican-plugins/tree/master/liquid_tags)
Simply clone the plugins and add the folders to the plugins folder

I have also added comment support using Disqus, as well as changing the theme to bootstrap3, which plays very well with the liquid tags plugin. Once you register on the Discus website, add a line to the pelicanconf.py file to link the service.

Finally, the theme I am using here is the [pelican-bootstrap3](https://github.com/DandyDev/pelican-bootstrap3)

For any questions on the layout of the page, see the [github page]( nagordon.github.io) 
 as well as a google search for ```pelican ipython notebook``` and you will find many other good examples

## The Docs
[pelican](http://docs.getpelican.com/en/3.4.0/index.html) and [this](http://blog.getpelican.com/)  
[ghp-import](https://github.com/davisp/ghp-import)  

