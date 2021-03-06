from flask import Flask, redirect,render_template,request,flash, url_for
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///quote.db"
app.secret_key = "hello"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Inspiration(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    data = db.Column(db.String(150))

    def __repr__(self):
        return f"{self.id} - {self.data}"

# Lnding page
@app.route("/")
def index():
    return render_template("index.html")

# Gets an inspiration from a form and stores it in the database
@app.route("/inspire",methods=["POST","GET"])
def inspire():
    if request.method== "POST":
        data = request.form.get("data")
        if data:
            new_data = Inspiration(data=data)
            db.session.add(new_data)
            db.session.commit()
            return render_template("index.html")
    return render_template("inspire.html")

# Gets a random quote from the database
@app.route("/getinspired",methods=["GET","POST"])
def getinspired():
    inspiration_list = Inspiration.query.all()
    return render_template("getinspired.html", inspiration_list=inspiration_list) 

# Delete an entry in the database
@app.route("/getinspired/<int:inspiration_id>")
def delete(inspiration_id):
    delete_inspiration = Inspiration.query.filter_by(id=inspiration_id).first()
    db.session.delete(delete_inspiration)
    db.session.commit()
    return render_template("/index.html")

if __name__ == "__main__":
    app.run(debug=True)
