# run with git bash on windows

### use
# bash make_site.sh

# create a styled html file

pelican content -s publishconf.py

#git add site && git commit -m "site subtree commit"
#git add --all && git commit -m "added site source code"
#git subtree push --prefix site origin gh-pages
#rm site

# #-p    ##-p is a push
ghp-import output -m "updated doc webpage on gh-pages branch"

rm -rf output
rm *pyc

# add all master branch files
git add --all
git commit -m "auto add changes to master branch and updated gh-pages"
git push --all origin
