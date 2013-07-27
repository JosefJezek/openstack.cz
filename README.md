# openstack.cz

Source of small summary website about Czech (and Slovak) OpenStack community.

## Status: ACTIVE

Under active development and maintenance.

## How to Commit content

### Prepare environment for Pelican

[How to install environment](https://github.com/josefjezek/openstack.cz/blob/master/INSTALL.md)

### How to use [Shovel](https://github.com/dandesousa/pelican-shovel)

Prints short description of each command

```
shovel help
```

Prints help docs for command

```
shovel help post.new
```

Create post

```
shovel post.new --title "How to install OpenStack"
```

Lists all posts

```
shovel post.list
```

Case insensitive regex Search

```
shovel post.list 2013
```

Edits all posts with `programming` in the path, opens them in your editor

```
shovel post.edit programming
```

### Generate html for developing (while writing)

```
./generate.sh
```

### Serves website to 0.0.0.0 and port 8000

```
./serve.sh
```

Point your browser to localhost:8000 and you will see website.

### Publish website to GitHub

```
./publish.sh {commit message}
```

## Creative Commons License

Author [Josef Jezek](http://about.me/josefjezek)

This work is licensed under a [Creative Commons Attribution-NonCommercial-NoDerivs 3.0 Unported License](http://creativecommons.org/licenses/by-nc-nd/3.0/).

Uvedená práce (dílo) podléhá licenci [Creative Commons Uveďte autora-Neužívejte dílo komerčně-Nezasahujte do díla 3.0 Česko](http://creativecommons.org/licenses/by-nc-nd/3.0/cz/).

Static blog powered by [Pelican](http://docs.getpelican.com) on [GitHub Pages](http://pages.github.com).