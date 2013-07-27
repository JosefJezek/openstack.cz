#!/bin/sh

# Generate static html for developing (while writing).
# Author: [Josef Jezek](http://about.me/josefjezek)
# Usage: generate.sh [output directory]

OUTPUT=$1

if [ -f pelicanconf_local.py ]; then
	CONF=pelicanconf_local.py
else
	CONF=pelicanconf.py
fi

if [ $OUTPUT ]; then
    pelican -s $CONF -o $OUTPUT
else
    pelican -s $CONF
fi