#!/bin/sh

# Publish a Pelican site to master and gh-pages branch on GitHub.
# Author: [Josef Jezek](http://about.me/josefjezek)
# Usage: publish.sh {commit message}

MESSAGE=$1

# git checkout master
git add -u .
git commit -m "$MESSAGE"
git push origin master

rm -rf output
pelican -s publishconf.py
ghp-import -pm "$MESSAGE" output
