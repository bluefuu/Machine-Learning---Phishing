import requests
import tldextract

url = "https://revolution-admin-100002030038264578189.tk/checkpoint_next.php"

def cookie_domain(url):
    try:
        r = requests.get(url, timeout=2)
        ds = r.cookies.list_domains()
        if not ds:
            return None
        else:
            return ds[0]
    except:
        return None

def tld(url):
    d = tldextract.extract(url)
    return d.domain

def isPhish(url):
    cd = cookie_domain(url)
    d = tld(url)

    
    if cd is None:
        print("No cookie")
        return 0
    else:
        print('Cookie domain: ' + cd)
        print('URL: ' + d)
        if (d in cd) or (cd in d):
            return 0
        else:
            return 1

