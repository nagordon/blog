# -*- coding: utf-8 -*-
"""

# delete remote branch
git push origin --delete gh-pages

# delete local branch 
git branch -D gh-pages

# force a push
git push origin master --force


### generate site
pelican content -s pelicanconf.py

### create a development server that updates when changes are detected
make devserver
# stop 
./develop_server.sh stop


# generate the site and push it to github
make github



### automatically create CNAME file
cmds = ["git checkout gh-pages",
		"echo 'ifcuriousthenlearn.com' > CNAME",
	    "git add CNAME",
		"git commit -m 'Added CNAME'",
		"git push origin gh-pages"]

for k in cmds:
	os.system(k)
	
pelican content -o output -s pelicanconf.py
ghp-import output
git push --all origin
#git push origin master
#git push origin gh-pages	
	
"""

import os
os.system("pelican content")
os.system("ghp-import output")
os.system("git add --all")
os.system("git commit -m 'added new content to blog'")
os.system('git push --all origin')

