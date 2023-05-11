from flask import Flask,render_template
app=Flask(__name__)
@app.route("/")
def index():
    name="aswin"
    return render_template('sample2.html', n=name)
if __name__ in "__main__":app.run(debug=True)
