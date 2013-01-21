#!/usr/bin/env python
# coding=utf-8

def fn(value):
    """
    Return 'value'.
    
    >>> fn(1)
    1
    >>> fn(2)
    2
    >>> fn(3)
    3
    """
    return value


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    
