#!/usr/bin/env python
# coding=utf-8

import ez_setup
ez_setup.use_setuptools()

from setuptools import setup, find_packages


setup(name='my_program',
      version='0.0.1',
      author='My Name',
      author_email='my@mail.com',
      url='http://www.my_program.org',
      download_url='http://www.my_program.org/files/',
      description='Short description of my_program...',
      long_description='Short description of my_program...',

      #py_modules=['my_program'],
      #package_dir={'': 'my_program'},
      packages = find_packages(),
      include_package_data = True,
      package_data = {
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst'],
        # And include any *.msg files found in the 'hello' package, too:
        'my_program': ['*.msg'],
        'my_program/reports': ['*.html', '*.css'],
      },
      exclude_package_data = { '': ['README.txt'] },
      
      scripts = ['bin/my_program'],
      #eager_resources = ['my_program/reports/plat_p.html'],
      
      #provides=['my_program'],
      keywords='python tools utils internet www',
      license='GPL',
      classifiers=['Development Status :: 5 - Production/Stable',
                   'Natural Language :: English',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python :: 2',
                   'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
                   'License :: OSI Approved :: GNU Affero General Public License v3',
                   'Topic :: Internet',
                   'Topic :: Internet :: WWW/HTTP',
                  ],
                  
      setup_requires = [],
      install_requires = ['setuptools'],
      
      #test_loader='unittest:TestLoader',
      test_suite = 'my_program.test.test.suite'
     )
