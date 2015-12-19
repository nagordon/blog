# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 18:49:47 2015

@author: neal

# delete remote branch
git push origin --delete gh-pages


"""

import os

#os.system('pelican content -s pelicanconf.py')

cmds = ["git checkout gh-pages",
		"echo 'ifcuriousthenlearn.com' > CNAME",
	    "git add CNAME",
		"git commit -m 'Added CNAME'",
		"git push origin gh-pages"]

for k in cmds:
	os.system(k)