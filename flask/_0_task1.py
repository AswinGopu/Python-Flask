
from flask import Flask
app=Flask(__name__)
@app.route("/age/<int:n>")
def index(n):
    if n % 2==0:
        return "<h1> %s Is EVEN NUMBER</h1>"%n
    else:return "<h1> %s Is ODD NUMBER</h1>"%n
app.run(debug=True)