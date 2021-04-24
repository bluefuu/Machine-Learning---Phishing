import pandas

import sys
import os
ROOT_DIR = os.path.dirname(os.path.abspath("")) + '\\functions'
sys.path.append(ROOT_DIR)


import ygdom as yd
import badcookie as bc
import foreignlinks as fl
import foreignfavi as ff
import nodns
import badssl as bs


dfp = pandas.read_csv('dataset\phishing.csv')
#list(df)
dfp = dfp.drop(columns=['phish_id', 'online','phish_detail_url','submission_time','verified','verification_time', 'target'])
dfp['is_phishing'] = "1"
dfp = dfp.sample(frac = 0.055)
dfp.to_csv('phishingclean.csv',index=False)

dfl = pandas.read_csv('dataset\legitimate.csv', names=['url'])
dfl['is_phishing'] = "0"
dfl = dfl.sample(frac = 0.18)

bigData = dfp.append(dfl, ignore_index=True)

#1 blacklist
dfb = pandas.read_csv('dataset\\blacklist.csv', names=['url'])
bigData['blacklist'] = bigData.url.isin(dfb.url).astype(int)

#2 ip_address
bigData['is_ipaddress'] = bigData.url.str.match('^(http|https)://\d+\.\d+\.\d+\.\d+\.*').astype(int)

#3 is_at
sub = '@'
bigData.loc[bigData['url'].str.find(sub) > 0 , 'is_at'] = 1
bigData.loc[bigData['url'].str.find(sub) <= 1 , 'is_at'] = 0

#4 multi-domain
bigData.loc[bigData['url'].str.count('\.') > 3 , 'mulit-domain'] = 1
bigData.loc[bigData['url'].str.count('\.') <= 3 , 'mulit-domain'] = 0
#bigData['multi-domain'] = bigData['url'].str.count('\.')

#5 url_length
bigData.loc[bigData['url'].str.len() >= 74 , 'url_length'] = 1
bigData.loc[bigData['url'].str.len() < 74 , 'url_length'] = 0
#bigData['url_length'] = bigData['url'].str.len()

#6 domain_age
bigData['yg_domain'] = bigData['url'].apply(yd.isPhish)

#7 badcookie
bigData['bad_cookie'] = bigData['url'].apply(bc.isPhish)

#8 foreignlinks
bigData['foreign_links'] = bigData['url'].apply(fl.isPhish)

#9 foreignfavicon
bigData['mismatch_favi'] = bigData['url'].apply(ff.isPhish)

#10 no_dns
bigData['no_dns'] = bigData['url'].apply(nodns.isPhish)

#11 https_issuer
bigData['bad_ssl'] = bigData['url'].apply(bs.isPhish)

bigData.to_csv('dataset\\features.csv')