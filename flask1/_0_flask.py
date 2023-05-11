from flask import Flask
app=Flask(__name__)
@app.route("/")
def index():
    return "welcome"
@app.route("/home")
def home():
    return "welcome home"   
@app.route("/about")
def about():
    return "<h1 style=color:red>welcome about</h1>"     
app.run(debug=True)    