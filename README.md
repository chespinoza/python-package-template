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
* setup.py - all distutils, setuptools features
* tests - unittest, pytest
* .tar.gz - source generation
* .deb generation
* _.rpm generation_
* virtualenv - install and put package into it


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


Please, send ideas - [here](https://github.com/vital-fadeev/python-package-template/issues/new)  
Send issues - [here](https://github.com/vital-fadeev/python-package-template/issues/new)  
You find bug? - post it to me [here](https://github.com/vital-fadeev/python-package-template/issues/new)  

