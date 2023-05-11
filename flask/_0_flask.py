# pip install flask


from flask import Flask

app = Flask(__name__)
# @app.route("/http://127.0.0.1.5000")
@app.route("/")
def index():
    return "<h1>welcome</h1>" 
@app.route("/home")
def home():
    return "<h2 style='color:red'>hello home</h2>"
@app.route("/about")
def about():
    return "<h1 style='color:blue'>about</h1>"

app.run()    
