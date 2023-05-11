
from flask import Flask,render_template,make_response,request
app=Flask(__name__)
@app.route("/")
def index():
    return render_template("sample3.html")
@app.route("/home",methods=["POST"])
def home():
    data=request.form
    res=make_response(render_template("sample3.html"))
    res.set_cookie("usarname",data["uname"])    
    res.set_cookie("password",data["pass"])
    return res
@app.route("/view")
def view():
    uname=request.cookies.get("usarname")    
    passwd=request.cookies.get("password")   
    return "<h1>username : %s  password : %s</h1>"%(uname,passwd) 
    
if __name__ in "__main__":app.run(debug=True)        