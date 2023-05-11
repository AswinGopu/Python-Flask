
from flask import Flask,render_template,redirect,session,request
app = Flask(__name__)
app.secret_key="secret"
@app.route("/")
def home():
    return render_template("sample4.html")
@app.route("/store", methods=["POST"])   
def store():
    data=request.form
    session["username"] = data["uname"]
    session["password"] = data["pass"]
    return redirect("/view")
@app.route("/view")
def view():
    if "username" in session:
        username = session["username"]    
        passwd = session["password"]
        return "<h1>username : %s  ,  password: %s </h1>"%(username,passwd) 
    else:
        return "<h1 style= color:red>Not found.....!</h1>"
@app.route("/delete")
def delete():
    msg = " "
    if "username" in session:
        session.pop("username",None)
        session.pop("password",None)
        msg = "session cleared"
        return render_template("sample4.html",msg = msg)
    else:
        msg = "not found....!"
        return render_template("sample4.html",msg = msg)

if __name__ in "__main__":app.run(debug=True)    
