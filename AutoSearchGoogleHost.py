#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
    Copyright 2011 timger
    
    +Author timger
    +Gtalk&Email yishenggudou@gmail.com
    +Msn yishenggudou@msn.cn
    +Weibo @timger http://t.sina.com/zhanghaibo
    +twitter @yishenggudou http://twitter.com/yishenggudou
    Licensed under the MIT License, Version 2.0 (the "License");
'''

import os
import sys
import subprocess


__author__ = 'timger & yishenggudou@gmail.com'
__license__ = 'MIT'
__version__ = (0,0,0)

#GDomain = ['google.com','g.cn','google.com.hk']
GDomain = ['g.cn']
HOSTS = os.path.join(os.getcwd(),'hosts','hosts')


def SearchNewIP():
    import re
    IPS = []
    for i in GDomain:
        res = subprocess.Popen(['nslookup',i],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        f=res.stdout.read()
        IPS.append(re.findall('Address\:.(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\\n',f))
    return IPS

def CheckIP(ip):
    import urllib2
    try:
        res = urllib2.urlopen('http://'+ip).read()
        return True
    except:
        return False
        
def UpdateIP(ip):
    import re
    Gdocs =['docs.google.com','docs0.google.com','docs1.google.com','docs2.google.com','docs3.google.com','spreadsheets.google.com','spreadsheets0.google.com','spreadsheets1.google.com','spreadsheets2.google.com','spreadsheets3.google.com']
    fhosts = open(HOSTS,'rw')
    hosts = fhosts.read()
    for i in Gdocs:
        regx = '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}.*?%s' %i
        news = '%s %s' %(ip,i)
        hosts = re.sub(regx,news,hosts)
    fhosts.write(hosts)
    fhosts.close()

def mian()
    IPS = SearchNewIP()
    IP = filter(CheckIP,IPS)[0]
    UpdateIP(IP)

if __name__ == "__mian__":
    main()

    

