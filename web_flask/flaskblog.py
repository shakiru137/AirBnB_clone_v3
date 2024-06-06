#!/usr/bin/env python3
from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return "<h1 style='color: blue;'>HOME PAGE</h1>"

@app.route('/about')
def about():
    return "<h2>ABOUT PAGE</h2>"

@app.route('/home/name')
def home_with_name():
    name = input("Enter your name: ")
    return f"<h3>Hello {name}</h3>"

if __name__ == "__main__":
    app.run(debug=True)

