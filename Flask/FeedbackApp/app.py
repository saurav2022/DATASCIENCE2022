from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql://postgres:postgres@localhost/renault"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
app.app_context().push()


class Feedback(db.Model):
    __tablename__ = "feedback"
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(100), unique=True)
    dealer = db.Column(db.String(100))
    rating = db.Column(db.Integer)
    comments = db.Column(db.String(200))

    def __init__(self, customer, dealer, rating, comments):
        self.customer = customer
        self.dealer = dealer
        self.rating = rating
        self.comments = comments


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    try:
        customer = request.form["customer"]
        dealer = request.form["dealer"]
        rating = request.form["rating"]
        comments = request.form["comments"]

        data = Feedback(customer, dealer, rating, comments)
        db.session.add(data)
        db.session.commit()

        return render_template("success.html", customer=customer)
    except Exception as e:
        print(e)
        return f"Encountered error in submission :{e}"


if __name__ == "__main__":
    app.run(debug=True)
