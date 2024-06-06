#!/usr/bin/python3
from flask import Flask
from flask import render_template

app = Flask(__name__)
@app.route('/', strict_slashes=False)
def home_page():
    name = "Yusuf Shakiru Oluwasegun AKA GodOfThermo"
    return render_template("index.html", name=name)
if __name__ == '__main__':
    app.run(host='172.21.55.138', port=8000, debug=True)
