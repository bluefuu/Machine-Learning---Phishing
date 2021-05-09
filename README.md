![banner_small.png](banner_small.png)

> 2021 Cyber Security Capstone Project
> 
> Kim Nguyen
## Objective
Phishing websites are fake websites created by malicious people with the intention of stealing user's personal data. Detecting and identifying a phishing website is a complex problem as it takes many factors into account. This project is an attempt to create a web app that identifies phishing websites using Machine learning.

## Dataset
Datasets have been imported from online sources such as Phishtank.org (http://phishtank.org/)
which is a community where members submit a suspected website including relevant information and gets verified through voting by  a required number of people. A total of 1500 verified phishing websites have been collected on the mentioned source. In addition to that, 1500 legitimate websites have also been collected from Domcop.com ( https://www.domcop.com/) where a collection of most popular and trusted websites can be found. 

## Features
In capturing the characteristics of phishing websites, a set of variables are used and these are called features. By defining the features, it allows the application to capture the characteristics of a phishing website and determine if it is legitimate or not. <br />

The application initially used eleven (11) functions for each website from the dataset collection of 3000 websites. These websites have their data extracted based on the features which are categorised by 1 and 0 - 1 for being legitimate and 0 for being suspicious. This data is saved as a .csv file which will be used for decision making and for analysing the subset based feature. 
<br /><br />

1. **Blacklist** <br />
Websites that are already in the blacklist database is considered phishing.
2. **IP address** <br />
Legitimate companies rarely use IP addresses as links. Some phishing attacks are hosts from compromised machines which may not have DNS entries and the simplest way is to refer to them by IP address. Hence, any email that contains  ip addresses and flagged as phishing.
3. **@ symbol** <br />
The browser ignores everything before the @ symbol in a URL. Users can be fooled by a URL, expecting the browser will load what they see at first glance. However, the browser will only execute whatever is after the @ which may lead the user to a malicious page. 
4. **Multi domain** <br />
A normal domain will have a domain name and a sub-domain e.g. https://subdomain.example.com. Any URL that has more than this is trying to hide it's suspicious domain or tries to imitate a legitimate website.. http://vvvvvv.amazcn.co.jp.e560dfa112bb63b62d2b0f74f681d979ba30ad08d.ph/pc
5. **Long url** <br />
An attacker can use a long url to try and hide any suspicious part in their url.
6. **Domain Age** <br />
Domains that are used by attackers have  limited lifetime this is to avoid being detected. Using the WHOIS query, the domain creation and expiration date can be retrieved.
7. **Cookie** <br />
A cookie lets a website remember the user's logins and shopping cart but can also be abused by attackers to exploit personal data.  
8. **Webpage links** <br />
Phishing websites are usually a copy of a legitimate website. An attacker will not fully develop the website from scratch but rather borrow the code from the legitimate website. This results in using the same links as legitimate websites. Websites with over 50% of their links from a different domain are deemed suspicious.
9. **Favicon** <br />
A favicon is an icon that is used as an identity for a website or organisation. If a favicon loaded is from a different domain it is likely a phishing attempt.
10. **DNS record** <br />
Phishing websites highly unlikely to register its information. If the DNS record for the website is empty or not found, the website is classified as phishing.
11. **SSL certificates** <br />
Sites with SSL certificates or https give an impression that it is trustworthy, however, phishing websites nowadays can obtain a SSL certificate easily. Therefore, it is necessary to check the issuer of the certificate if it's from a trustworthy issuer. The trustworthy issuer list is extracted from the top 500 domains.

## Model & Training
In machine learning, there are two types of predictions, classification and regression. This project uses the classification method which is a supervised learning concept that categorises a set of data into classes. These classes are used for phishing detection in two categories which are legitimate or phishing. <br />

Machine learning has many algorithms that can be used to train the model. Decision tree is a popular model and have been proven to have the highest accuracy compared to others. A decision tree is a more complex if-else statement that is constructed like a tree. The model is constructed by feeding the dataset and splitting it into different nodes. The end nodes are called leaf which is what the model concluded to be the outcome. 

## Building the web application
In order to build the application, components have to be collected, imported, and sorted. This process includes acquiring the raw dataset which would then be imported into Python that used the Panda library to remove duplicates and empty fields. This step would provide more accuracy and quality of the data. <br />

Functions are defined to extract data from the dataset which would then be integrated into the Python module called DecisionTree by Avinash Kak that results in a working model that can be used for the web application. <br />


In order to develop the web application, Flask framework is used as the backend which would connect the webpage to the flask. The said framework is ideal because the web application doesn’t need a database. <br />

By creating a webpage, it allows to take an input from the user which would then be sent to Flask. This process includes validating if what is being received is a URL. Once the url has been validated, it will be directed to the decision tree model and classify if the website is a legitimate one or a phishing one based on the percentage and create an output of the result.

## Demo
Click here for demo of the app https://phishornah.herokuapp.com/ <br />

### Current limitations
This is only a demonstration and is not fully functioning app. Inaccuracy can be identified  when a URL with long paths is tested.. In order to create a more accurate result, more features are needed to be introduced and with existing features; algorithms need to be refined. <br />
Additional improvement would be implementing deep learning. Deep learning is a subset of machine learning that builds an “artificial neural network”. This allows the model to learn and make intelligent decisions on it’s own. In other words, deep learning continues to learn when the application is running whereas for a decision tree, once the model is built it stops learning. 




