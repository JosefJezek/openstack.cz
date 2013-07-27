#!/bin/sh

# Publish a Pelican site to master and gh-pages branch on GitHub.
# Author: [Josef Jezek](http://about.me/josefjezek)
# Usage: publish.sh {commit message}

MESSAGE=$1

if [ -f pelicanconf_local.py ]; then
	CONF=pelicanconf_local.py
else
	CONF=pelicanconf.py
fi

git checkout master
git add .
git commit -m "$MESSAGE"
git push origin master

rm -rf output
pelican -s $CONF
ghp-import -pm "$MESSAGE" output
