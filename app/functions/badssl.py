import csv
import json
from ssl_checker import SSLChecker

import sys
import os

ROOT_DIR = os.path.dirname(os.path.abspath("")) + "\sort_data\dataset"
sys.path.append(ROOT_DIR)

filename = ROOT_DIR + "\ssl_issuers.csv"

url = "https://thispointer.com/"

SSLChecker = SSLChecker()

list_issuers = []

with open(filename,'r') as data:
   for line in csv.reader(data):
       list_issuers.append(line)

args = {
    'hosts': [url]
}



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

def isPhish(url):
    issuer = get_issuer(url)
    bad_ssl = 1

    if issuer:
        print("issuer: " + issuer)
        for x in list_issuers:
            if issuer in x:
                bad_ssl = 0
                exit
    else:
        print("No ssl")
        
    return bad_ssl

