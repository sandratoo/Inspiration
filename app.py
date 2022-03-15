from re import T
from flask import Flask,render_template,request,flash 

app = Flask(__name__)
app.secret_key = "hello"

@app.route("/hello")
def index():
    flash("What's your name?")
    return render_template("index.html")

@app.route("/greet",methods=["POST","GET"])
def greet():
    name = request.form["name"]
    flash(f"Hello {name} nice to see you!")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)