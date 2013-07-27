#!/bin/sh

# Auto generate static html for developing (while writing).
# Prerequisite: sudo apt-get install inotify-tools
# Author: [Josef Jezek](http://about.me/josefjezek)
# Usage: autogenerate.sh [output directory]

OUTPUT=$1

generate() {
  notify-send "Generating site..."
  ./generate.sh $OUTPUT
}

generate

while inotifywait -r -e create,move,modify,delete --excludei "\.git|output" .
do
   generate
done