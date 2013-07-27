#!/bin/sh

# Serve directory to 0.0.0.0 and defined port.
# Author: [Josef Jezek](http://about.me/josefjezek)
# Usage: serve.sh [directory]

PORT=8000
DIRECTORY=$1

if [ $DIRECTORY ]; then
    cd $DIRECTORY
else
    cd output
fi

# Detect Python version
result=`python -c 'import sys; print("%i" % (sys.hexversion<0x03000000))'`

if [ $result -eq 0 ]; then
    # Python version is >= 3
    python -m http.server $PORT
else 
    # Python version is < 3
    python -m SimpleHTTPServer $PORT
fi
