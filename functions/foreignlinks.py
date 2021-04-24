import tldextract
from bs4 import BeautifulSoup
import urllib.request


def get_links(url):
    links = []
    try:
        html = urllib.request.urlopen(url, timeout=3)
        soup = BeautifulSoup(html, "html.parser")

        for link in soup.findAll('a'):
            if link.has_attr('href'):
                links.append(link['href'])
    except:
        pass
    return links

def get_domain(url):
    d = tldextract.extract(url)
    return d.domain

def dom_links(links,url):
    count = 0
    if links:
        d = get_domain(url)
        for link in links:
            if link:
                if d in link:
                    count = count + 1
    return count

def count_path(links):
    count = 0
    if links:
        for link in links:
            if link:
                if '/' in link[0]:
                    count = count + 1
    return count

def isPhish(url):
    links = get_links(url)
    total = len(links)
    dom = dom_links(links, url)
    path = count_path(links)
    

    if not links:
        print("No response")
        return 0
    else:
        foreign = total - (dom + path)
        ratio = foreign/total
        print('Path: ' + str(path))
        print('Domain: ' + str(dom))
        print('Total: ' + str(total))
        if ratio > 0.5:
            print("Ratio: " + str(ratio))
            return 1
        else:
            print("Ratio: " + str(ratio))
            return 0

    