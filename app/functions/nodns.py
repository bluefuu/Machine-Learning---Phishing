import tldextract
import dns.resolver

url = "https://www.facebook.com"

def get_domain(url):
    return tldextract.extract(url).domain

def get_suffix(url):
    return tldextract.extract(url).suffix

def get_url(url):
    d = get_domain(url)
    s = get_suffix(url)
    return  d + "." + s

def isPhish(url):
    u = get_url(url)
    resolver = dns.resolver.Resolver()
    resolver.timeout = 3

    try:
        d = resolver.resolve(u)
        print('url: ' + url + ", dns exist.")
        return 0
    except:
        print('url: ' + url + ", no dns.")
        return 1
