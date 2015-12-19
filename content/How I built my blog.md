Title: My First Blog
Date: 2015-02-25
Modified: 2015-12-19
Category: Tutorials
Tags: tutorial, python, pelican
Slug: my-first-blog
Authors: Neal Gordon
Summary: How the heck I built a blog
 
My first whimsical thought of creating a blog was, how hard can it be? Well, as it turns out, I found it it is harder than expected. But, here it is, and here I am. This is a rough outline to how I got my blog working and how I update. I started with a github page using jekyll, but decided that I really would like ipython notebook support, so that left me with [Nickola](http://getnikola.com/) or [Pelican](http://docs.getpelican.com/en/3.5.0/#). I thought the Pelican documentation looked easier, so I went with it. I have also changed my blog to be a github project page rather than a user page. This changed my workflow so I have updated to reflect that.

## setup
I am running a windows 8 laptop with a  [Linux-Mint](http://www.linuxmint.com/) virtual machine using [VirtualBox ](https://www.virtualbox.org/). 

Lets update all the software on our virtual machine with 

```bash
# updates
sudo apt-get update && sudo apt-get upgrade

# we need git to use github
sudo apt-get install git
```

Now lets install python 3.x. I really like using miniconda for my python management. You can install it with the following commands.

```bash
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
# follow the commands to install
```

Restart the terminal and try running '''ipython'''. If it doesn't work, then figure out why before continuing.

Next, lets install the software we need to build the blog. I have decided to work with python 3.x, which limits some of the plugins, but I try to develop in python as much as possible.

```bash
conda install pip, ipython-notebook
pip install pelican, Markdown
# for github blogs, this tool makes it very easy to update the blog
pip install ghp-import
```

[ghp-import](https://github.com/davisp/ghp-import) is a great too for building blogs on github. For project pages(if you don't know what this is, go find out because you may have trouble posting your blog to github). Basically, the ```master``` branch stores the content of the blog and the ```gh-pages``` stores the actual site being hosted. 
Now we need a github account and a repository to host our site and source content, [repository](https://github.com/nagordon/ifcuriousthenlearn). We can roll out a site immediately with githubs automatic site building tools that utilize ruby. Unless I add a custom url (see below), the site will be hosted at http://nagordon.github.io/ifcuriousthenlearn

Once you have created a repository on github, in the bash terminal, clone the github repository to your local computer 
```bash
git clone https://github.com/nagordon/ifcuriousthenlearn.git
```

this will create a directory ```ifcuriousthenlearn``` that will have all the website content. The [pelican quickstart](http://docs.getpelican.com/en/3.6.3/quickstart.html) is great for playing around with new sites. 

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
Here is the end of the post!!

```
The tags will automatically create groups at the top of your webpage once it is built

Once you have your *.md, we need to generate the static html files that will be the blog
```bash

# I first use this to tweak the site and it constantly updates my changes locally
make devserver
# and to stop
./develop_server.sh stop

#once the site is how you like it run these commands to push to github.
pelican content -o output -s pelicanconf.py
ghp-import output
git push --all origin

```


## Next Steps
One of the things I really like about pelican is I can embed [ipython notebooks](http://nbviewer.ipython.org/) into the blog post. To do so, just check out this [plugin](https://github.com/danielfrg/pelican-ipynb). This allows my to store each post in a notebook, and use python 3.

I have also added comment support using Disqus, as well as changing the theme to bootstrap3, which plays very well with the liquid tags plugin. Once you register on the Discus website, add a line to the pelicanconf.py file to link the service.

Finally, the theme I am using here is the [pelican-bootstrap3](https://github.com/DandyDev/pelican-bootstrap3)

For any questions on the layout of the page, see the [github page]( nagordon.github.io) 
 as well as a google search for ```pelican ipython notebook``` and you will find many other good examples

## Custom URL 

I also added a custom domain name with godaddy. It cost $10 and was relativley easy. For github project pages, here is a general process for setting that up. 

Set up godaddy.
![](/fig/godaddy_github_pages_setup.png "Setting up godaddy")

Add '''content/extra/CNAME''' file to website source code and add  the url you want. In this case the file contents are ```ifcuriousthenlearn.com```

Now add the configurations to the ```pelicanconf.py```

```
STATIC_PATHS = ['extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}
SITEURL = 'http://ifcuriousthenlearn.com'
```



## The Docs
[pelican](http://docs.getpelican.com/en/3.4.0/index.html) and [this](http://blog.getpelican.com/)  


