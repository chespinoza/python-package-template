python-package-template
=======================

Start template for python package.


### Concept ###
* **One location for settings** - all settings specified in **setup.py**
* **Simple usage** - one command: **make**


### Contains ###
* setup.py
* Makefile
* tests
* source distributive generation
* .deb generation
* _.rpm generation_


### More commands ###
* **make test** - run all tests
* **make deb** - build Debian package
* **make source** - build source tarball
* **make daily** - make daily snapshot
* **make install** - install program
* **make init** - install all requirements
* **make clean** - clean project, remove *.pyc and other templorary files
