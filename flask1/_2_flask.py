from flask import Flask,redirect,url_for
app=Flask(__name__)
@app.route("/")
def index():
    return "<h1>welcome</h1>"
@app.route("/home")
def home():
    return "<h1>welcome home</h1>"
@app.route("/redirect") 
def redict():
    return redirect(url_for("index"))
app.run(debug=True)           
