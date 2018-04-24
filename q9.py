
from flask import Flask

from flask import render_template

import random

app = Flask(__name__)

@app.route("/")

def quotes():
    with open("inspiration.txt",encoding="utf8") as fp:
        a=fp.readlines()
    ran=random.randint(0,len(a)-1)
    quote=a[ran].replace('\n','')
    return render_template('quotes.html', quote=quote)
