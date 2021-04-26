# Phishing Website Detection using Machine Learning
## Objective
Phishing websites are fake websites created by malicious people with the intention of stealing user's personal data. Detecting and identifying a phishing website is a complex problem as it takes many factors into account. This project is an attempt to create a web app that identifies phishing websites using Machine learning.

## Dataset
**Phishing websites:** 500 random websites were taken from http://phishtank.org/ <br />
**Legitimate websites:** 500 random websites were taken from https://www.domcop.com/

## Features
This is a set of features that is used to detect phishing website. Each website in the dataset has its data being extracted base on the features. The extracted data are in 1 and 0, 1 for being legitimate and 0 for being suspicious. Data are saved as a .csv file used to train the machine learning.<br /><br />

1. **Blacklist** <br />
Websites that are already in the blacklist database is considered phishing.
2. **IP address** <br />
Legitimate websites is known to have a domain name. Any URL that includes an IP address is suspicious and can be stealing your data.
3. **@ symbol** <br />
The browser ignores everything before the @ symbol in a URL. User can be fooled by URL expecting the browser will load what they see at first glance. However, the browser will only execute whatever is after the @ which may lead the user to a malicious page.
4. **Multi domain** <br />
A normal domain will have a domain name and a sub-domain e.g. https://subdomain.example.com. Any URL that has more than this is trying to hide it's domain and have a domain that tries to imitate a legitimate website. http://vvvvvv.amazcn.co.jp.e560dfa112bb63b62d2b0f74f681d979ba30ad08d.ph/pc
5. **Long url** <br />
An attacker can use a long url to try and hide any suspicious part in their url.
6. **Domain Age** <br />
Most of the time phishing websites are short-lived and trustworthy websites existed for a long period of time. Using whois database, domain information is being retreived to determine the age of the website. If a website is 6 month young it is considered suspicious. 
7. **Cookie** <br />
A cookie lets a website remembers the user's logins and shopping cart but can also be abused by attacker to exploit personal data.  
8. **Webpage links** <br />
Phishing websites are usually a copy of a legitimate website. An attacker will not fully developed the website from scratch but rather borrow the code from the legitimate website. This result in using the same links as legitimate website. Websites with over 50% of their links from a different domain is deemed suspicious. 
9. **Favicon** <br />
A favicon is an icon that used as an identity for a website or organisation. If a favicon loaded is from a different domain it is likely a phishing attempt.
10. **DNS record** <br />
Phishing websites highly unlikely to register its information. If the DNS record for website is empty or not found the website is classified as phishing.
11. **SSL certificates** <br />
Sites with SSL certificates or https give an impression that it is a trustworthy, however, phishing website nowdays can obtain a SSL certificate easily. Therefore, it is necessary to check the issuer of the certificate if its from a trustworthy issuer. The trustworthy issuer list is extracted from the top 500 domains.

## Model & Training
Dataset = classification problem. <br />
URL input is classified as phishing or legitimate. <br />
Machine learning model used Decision Tree.

## Demo
Click here for demo of the app https://phishornah.herokuapp.com/ <br />
### Current limitations
This is only a demonstration and is not fully functioning. 
The app current doesn't support URL with paths and will not returned an accurate result.




