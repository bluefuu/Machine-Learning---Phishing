import pandas
import json
from ssl_checker import SSLChecker

SSLChecker = SSLChecker()

df = pandas.read_csv('others\\topwebsites.csv', names=['url'])

def get_issuer(url):
    args = {
        'hosts': [url]
    }

    try:
        r = SSLChecker.show_result(SSLChecker.get_args(json_args=args))
        data = json.loads(r)
        dom = next(iter(data))
        return data[dom]['issuer_o']
    except:
        return None
    
df['issuer'] = df['url'].apply(get_issuer)

df = df.drop(columns=['url'])
df = df.drop_duplicates(subset=['issuer'])
df.to_csv('ssl_issuers.csv', index=False)
