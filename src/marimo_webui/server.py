from flask import Flask, render_template

from marimo_webui.tempreture import getTempreture

app = Flask(__name__)

@app.route("/")
def index():
    tempreture = getTempreture()
    return render_template("index.html", tempreture=tempreture)