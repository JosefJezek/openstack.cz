Title: Welcome All
Slug: welcome-all
Date: 2013-07-22 19:19
Category: Python
Tags: pelican, publishing
Author: Josef Jezek
Media: openstack.jpg
Media_type: image
Summary: Short version for index and feeds

# How to install environment

## Install Pelican on Ubuntu

### Installing Python tools

```
sudo apt-get install python-setuptools inotify-tools
sudo easy_install pip
sudo pip install virtualenv virtualenvwrapper
```

`vi ~/.bashrc` (maybe `virtualenvwrapper.sh` is in other location, change if necessary)

```sh
# Virtualenvwrapper
export WORKON_HOME=$HOME/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
```

Load file `.bashrc`

```
source ~/.bashrc
```

Create [virtualenv](http://www.virtualenv.org/en/latest/) with [virtualenvwrapper](http://www.doughellmann.com/projects/virtualenvwrapper/)

```
mkvirtualenv blog
workon blog
```