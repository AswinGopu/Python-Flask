from flask import Flask
app=Flask(__name__)
@app.route("/age/<int:n>")
def index(n):
    if n<=10:
        return "<h1>%s little boy</h1>"%n
    elif n<=30:
        return "<h1>%s yongster</h1>"%n
    elif n<=40:
        return "<h1>%s mature</h1>"%n
    else:
        return "<h1>%s older</h1>"%n            
app.run(debug=True)        
