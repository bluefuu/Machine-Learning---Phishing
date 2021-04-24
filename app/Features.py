import sys
import os
import csv
import re


ROOT_DIR = os.path.dirname(os.path.abspath(""))
path = ROOT_DIR + '\\functions'
sys.path.append(path)

import ygdom as yd
import badcookie as bc
import foreignlinks as fl
import foreignfavi as ff
import nodns
import badssl as bs

filename = ROOT_DIR + "\\app\data\\blacklist.csv"

blacklist = []

with open(filename,'r') as data:
    for line in csv.reader(data):
        blacklist.append(line)

#create an array with the 11 features
class Feature:
    def __init__(self, url):
        self.url = url

    def isBlacklist(self):
        phish = False
        for i in blacklist:
            if self.url in i:
                phish = True
                exit
        value = int(phish)
        return "blacklist = " + str(value)

    def hasIPaddress(self):
        phish = False

        if re.match('^(http|https)://\d+\.\d+\.\d+\.\d+\.*', self.url):
            phish = True
        
        value = int(phish)
        return "is_ipaddress = " + str(value)

    def hasAt(self):
        phish = False
        isAt = self.url.find('@')

        if isAt > 0:
            phish = True

        value = int(phish)
        return "is_at = " + str(value)

    def multiDomain(self):
        phish = False
        c = self.url.count('\.')

        if c > 3:
            phish = True

        value = int(phish)
        return "multi_domain = " + str(value)

    def longUrl(self):
        phish = False

        if len(self.url) >= 74:
            phish = True

        value = int(phish)
        return "url_length = " + str(value)

    def ygDom(self):
        value = yd.isPhish(self.url)
        return "yg_domain = " + str(value)

    def badCookie(self):
        value = bc.isPhish(self.url)
        return "bad_cookie = " + str(value)

    def foreignLinks(self):
        value = fl.isPhish(self.url)
        return "foreign_links = " + str(value)

    def foreignFavi(self):
        value = ff.isPhish(self.url)
        return "mismatch_favi = " + str(value)

    def noDns(self):
        value = nodns.isPhish(self.url)
        return "no_dns = " + str(value)

    def badSSL(self):
        value = bs.isPhish(self.url)
        return "bad_ssl = " + str(value)

    def getList(self):
        flist = []
        flist.append(self.isBlacklist())
        flist.append(self.hasIPaddress())
        flist.append(self.hasAt())
        flist.append(self.multiDomain())
        flist.append(self.longUrl())
        flist.append(self.ygDom())
        flist.append(self.badCookie())
        flist.append(self.foreignLinks())
        flist.append(self.foreignFavi())
        flist.append(self.noDns())
        flist.append(self.badSSL())
    
        return flist
