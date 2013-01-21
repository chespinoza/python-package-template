PYTHON=`which python`
NAME=my_program


all: check test source deb

dist: source deb

source:
	$(PYTHON) setup.py sdist

deb:
	$(PYTHON) setup.py --command-packages=stdeb.command bdist_deb

rpm:
	$(PYTHON) setup.py bdist_rpm --post-install=rpm/postinstall --pre-uninstall=rpm/preuninstall

install:
	$(PYTHON) setup.py install --install-layout=deb

test:
	unit2 discover -s $(NAME) -t .

check:
	find $(NAME) -name \*.py | xargs pylint --errors-only --reports=n
	# pep8
	# pyntch
	# pyflakes
	# pychecker
	# pymetrics

upload:
	$(PYTHON) setup.py sdist register upload
	$(PYTHON) setup.py bdist_wininst upload

init:
	pip install -r requirements.txt --use-mirrors

update:
	rm ez_setup.py
	wget http://peak.telecommunity.com/dist/ez_setup.py

daily:
	$(PYTHON) setup.py bdist egg_info --tag-date

clean:
	$(PYTHON) setup.py clean
	#$(MAKE) -f $(CURDIR)/debian/rules clean
	rm -rf build/ MANIFEST dist build my_program.egg-info deb_dist
	find . -name '*.pyc' -delete

