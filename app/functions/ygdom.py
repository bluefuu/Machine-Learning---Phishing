import whois
from datetime import datetime
from datetime import timedelta

def get_date(url):
    cdate = None
    try:
        w = whois.whois(url)
        cdate = w.creation_date
    except whois.parser.PywhoisError:
        pass
    except:
        pass
    return cdate

#check if date is a list type
def check_datetype(url):
    date = get_date(url)
    if isinstance(date, list):
        date = date[0]
    return date

def isPhish(url):
    date = check_datetype(url)
    yg = timedelta(days=182)
    tdate = datetime.today()

    if date is None:
        print('url: ' + url + ' no date')
        return 0
    else:
        try:
            age = tdate - date
            print("Url: " + url + " Age: " + str(age))
            if age < yg:
                return 1
            else:
                return 0
        except:
            return 0
