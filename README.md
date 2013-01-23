python-package-template
=======================

Start template for python package.  

### Usage ###
1. Run `git clone git://github.com/vital-fadeev/python-package-template.git`
2. Write Your nice code.


### Concept ###
* **One location for settings** - all settings specified in **setup.py** only
* **Simple usage** - one command: **make**


### Features ###
* distutils, setuptools setup.py features
* tests - unittest, pytest
* source .tar.gz. generation
* .deb generation
* _.rpm generation_
* installation virtualenv and put package into it


### More commands ###
* **make test** - run all tests
* **make deb** - build Debian package
* **make source** - build source tarball
* **make daily** - make daily snapshot
* **make install** - install program
* **make init** - install all requirements
* **make clean** - clean project, remove *.pyc and other templorary files
* **make deploy** - create vitrual environment


        .
        |-- bin
        |   `-- my_program
        |-- docs
        |   `-- doc.txt
        |-- my_program
        |   |-- data
        |   |   `-- some_data.html
        |   |-- submodule
        |   |   `-- __init__.py
        |   |-- __init__.py
        |   |-- helpers.py
        |-- tests
        |   |-- __init__.py
        |   |-- test_helpers.py
        |-- Makefile
        |-- CHANGES.txt
        |-- LICENSE.txt
        |-- README.md
        |-- requirements-dev.txt
        |-- requirements.txt
        `-- setup.py
