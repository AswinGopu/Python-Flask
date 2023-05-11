
from flask import Flask
app=Flask(__name__)
@app.route("/age/<int:n>")
def index(n):
    newYear = 2022
    n = newYear - n
    if n % 400==0 and n%100!=0 or n%4==0:
        return "<h1> %s IS LEAP YEAR</h1>"%n
    else:
        return "<h1> %s IS NOT LEAP YEAR</h1>"%n
app.run(debug=True)        
            
