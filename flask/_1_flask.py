
from flask import Flask
app=Flask(__name__)
@app.route("/")
def index():
    return "<h1>welcome</h1>"
@app.route("/home/<name>")
def home(name):
    return "<h1 style='color:red'>welcome back %s</h1>"%name  
@app.route("/about/age/<int:n>")
def about(n):
    return "<h1 style='color:blue'>about %s</h1>"%n
app.run(debug=True) 