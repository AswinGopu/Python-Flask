from flask import Flask,redirect,url_for
app=Flask(__name__)
@app.route("/")
def index():
    return "<h1 style=color:red>welcome</h1>"
@app.route("/home")
def home():
    return "<h1 style=color:blue>wlcome home</h1>"
@app.route("/about")
def about():
    return "<h1 style=color:green>wlcome about</h1>"  
@app.route("/redirect")
def redict():
    return redirect("/home")
app.run(debug=True)      