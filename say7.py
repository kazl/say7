#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
from BeautifulSoup import BeautifulSoup

page = urllib2.urlopen("http://www.say7.info")
print ('page: ', page)
soup = BeautifulSoup(page)
print('soup: ', soup)
menu = BeautifulSoup(soup.findAll(attrs={'class': 'menu5'}))

urllist = menu.findAll('a')
print(urllist)