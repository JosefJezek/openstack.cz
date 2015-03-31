# openstack.cz [![Gittip](https://raw.github.com/gittip/www.gittip.com/master/img-src/gittip-logo-32.png)](https://www.gittip.com/josefjezek)

[![Join the chat at https://gitter.im/JosefJezek/openstack.cz](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/JosefJezek/openstack.cz?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

Source of small summary website about Czech (and Slovak) OpenStack community.

## Status: ACTIVE

Under active development and maintenance.

## How to Commit content

[How to use Markdown](https://gist.github.com/5917040)

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

This work is licensed under a [Creative Commons Attribution 3.0 Unported License](http://creativecommons.org/licenses/by/3.0/).

Uvedená práce (dílo) podléhá licenci [Creative Commons Uveďte autora 3.0 Unported](http://creativecommons.org/licenses/by/3.0/deed.cs).

Static blog powered by [Pelican](http://docs.getpelican.com), which takes great advantage of [Python](http://python.org). Hosted on [GitHub Pages](http://pages.github.com).