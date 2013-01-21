#!/usr/bin/env python
# coding=utf-8

import unittest
import doctest
import glob
import os


def load_tests(loader, tests, pattern):
    ''' 
    Discover and load all unit tests in all files named ``test_*.py`` in ``.``
    '''
    suite = unittest.TestSuite()

    for all_test_suite in unittest.defaultTestLoader.discover('.', pattern='test_*.py'):
        for test_suite in all_test_suite:
            suite.addTests(test_suite)
            
    return suite


def suite():
    return load_tests(None, None, None)


if __name__ == '__main__':
    unittest.main(verbosity=2)
