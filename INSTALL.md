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

And to leave

```
deactivate
```

### Installing Pelican

```
sudo pip install pelican markdown ghp-import shovel
```

### Upgrading Pelican

```
sudo pip install --upgrade pelican markdown ghp-import shovel
```

## Install Git

```
sudo apt-get install git
```

### Setup Git

```
git config --global user.name "John Doe"
git config --global user.email johndoe@example.com
git config --global core.editor vi
```

### Clone Git repository

```
git clone https://github.com/josefjezek/openstack.cz
cd openstack.cz
```

### Create own settings file called settings_local.py

This file will not be commited to the git repository. Variables inside file being processed with Shovel by create post or page.

```
cp settings.py settings_local.py
```