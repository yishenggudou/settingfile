#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
    Copyright 2011 timger
    
    +Author timger
    +Gtalk&Email yishenggudou@gmail.com
    +Msn yishenggudou@msn.cn
    +Weibo http://t.sina.com/zhanghaibo

    Licensed under the Apache License, Version 2.0 (the "License");
'''

import os
import sys
import logging
import itertools
#http://docs.python.org/library/itertools.html
from xx import xx


DIR_PATH = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
NAME_FILE = os.path.relpath(__file__)


logger = logging.getLogger('octopus.libs.%s' %NAME_FILE)
logger.setLevel(logging.DEBUG)

sys.stdout = BASE_STDOUT
sys.path = sys.path+[]


__all__ = ['xx','xxx']
__version__ = (0,0,0)

assert Expression[, Arguments]
assert (Temperature >= 0),"Colder than absolute zero!"


class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)


def Print(func):
    def new_func(*args, **argkw):
        sys.stdout = STDOUT_FILE
        return func(*args, **argkw) #调用原函数继续进行处理
    return new_func
@A
def f(args):pass


class xx:
    """
    Returns a SystemStat describing memory usage, expressed in bytes.

    The returned object has the following accessors:

    - current(): memory currently used by this instance
    - average1m(): average memory use, over the last minute
    - average10m(): average memory use, over the last ten minutes
    - average1h(): average memory use, over the last hour
    
    write some doctest like this
    >>> from StringIO import StringIO
    >>> list(network_segment(StringIO(_sample_whois)))
    ['202.96.63.0/24', '203.93.123.0/24', '221.4.140.0/24', '221.5.250.0/24']
    """
    def __init__(self,**args):
        pass

    def __getitem__(self, key): 
        return self.data[key]

    def __setitem__(self, key, item): 
        self.data[key] = item

    def __repr__(self):
        return '<Class %s>' %'xx'

    def __str__(self):
        return 'some print content'

    def __del__(self):
        print 'leave the class'


def cube(x):
    """
    >>> cube(10)
    1000
    """
    return x * x







if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()


