from flask import Flask, render_template, request

import MLModel
import Features
import re

regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

app = Flask(__name__)

mlmodel = MLModel.MLModel()

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        url = request.form['search']
        isURL = (re.match(regex, url) is not None)
        if isURL:
            fl = Features.Feature(url)
            farray = fl.getList()
            r = mlmodel.test(farray)
            badge = ""
            title = ""
            if r is 'Safe':
                title = "Yay! Not Phish"
                badge = "bg-success"
            elif r is 'Threat':
                title = "Oh no Phish"
                badge = "bg-danger"
            else:
                title = "hmm not sure"
                badge = "bg-warning"

            return render_template("result.html", result=r, url=url, badge=badge, title=title)

        else:
            return render_template("invalid.html")
    else:
        return "nothing"


if __name__ == "__main__":
    app.run(debug=True)