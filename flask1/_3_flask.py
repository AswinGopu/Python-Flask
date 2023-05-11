from unicodedata import name
from flask import Flask,redirect,url_for
app=Flask(__name__)
@app.route("/")
def index():
    return "<h1>welcome</h1>"
@app.route("/home/<name>")
def home(name):
    return "<h1>welcome %s</h1>"%name
@app.route("/about")
def about():
    return "<h1>welcome about</h1>"
@app.route("/redirect")
def redict():
    newname="aswin"
    return redirect(url_for("home",name = newname))  
app.run(debug=True)            