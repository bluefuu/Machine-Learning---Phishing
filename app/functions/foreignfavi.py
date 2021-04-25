import requests
import tldextract


url = "https://lloyds.alert-device-activity.com/"

def get_dom(url):
    return tldextract.extract(url).domain

def get_suffix(url):
    return tldextract.extract(url).suffix

def get_protocol(url):
    if url.startswith('https'):
        return "https"
    elif url.startswith('http'):
        return "http"
    else:
        return None

def get_favicon(url):
    p = get_protocol(url)
    d = get_dom(url)
    s = get_suffix(url)

    if p and d and s:
        return p + "://www." + d + "." + s + "/favicon.ico"
    if (not p) and d and s:
        return "http://www." + d + "." + s + "/favicon.ico"
    else:
        return None

def isPhish(url):
    fav = get_favicon(url)
    print(fav)
    if fav:
        try:
            r = requests.get(fav, timeout=3)
            if r.status_code == 200:
                return 0
            else:
                return 1
        except:
            return 1
    else:
        return 1
