from flask import Flask, Response, request, render_template, redirect, url_for
import pymongo
import json
from bson.objectid import ObjectId

app = Flask(__name__)

try:
    mongo = pymongo.MongoClient(
        host="localhost", port=27017, serverSelectionTimeoutMS=1000
    )
    mongo.server_info()
    db = mongo.customers
except Exception as e:
    print(f"Error in connecting to Mongodb : {e}")


@app.route("/")
def home():
    return redirect(url_for("get_all_users"))


@app.route("/users", methods=["GET"])
def get_all_users():
    try:
        all_users = list(db.users.find())
        for user in all_users:
            user["_id"] = str(user["_id"])

        return render_template("index.html", users=all_users)

    except Exception as e:
        print(f"Error in getting users : {e}")
        return Response(
            response=json.dumps({"message": f"Error in getting users : {e}"}),
            status=400,
            mimetype="application/json",
        )


@app.route("/users", methods=["POST"])
def create_user():
    try:
        user = {
            "first_name": request.form["first_name"],
            "last_name": request.form["last_name"],
        }
        dbResponse = db.users.insert_one(user)
        print(f"Inserted user : {dbResponse.inserted_id}")
        return Response(
            response=json.dumps(
                {
                    "message": "Successfully created user",
                    "id": f"{dbResponse.inserted_id}",
                }
            ),
            status=200,
            mimetype="application/json",
        )
    except Exception as e:
        print(f"Error in creating user : {e}")
        return Response(
            response=json.dumps({"message": f"Error in creating user : {e}"}),
            status=400,
            mimetype="application/json",
        )


@app.route("/del_user/<id>")
def delete_user(id):
    try:
        db.users.delete_one({"_id": ObjectId(id)})
        return redirect(url_for("get_all_users"))

    except Exception as e:
        print(f"Error in creating user : {e}")
        return Response(
            response=json.dumps({"message": f"Error in deleting user : {e}"}),
            status=400,
            mimetype="application/json",
        )


@app.route("/users/<id>", methods=["PATCH"])
def update_user(id):
    try:
        dbResponse = db.users.update_one(
            {"_id": ObjectId(id)}, {"$set": {"first_name": request.form["first_name"]}}
        )
        return Response(
            response=json.dumps(
                {
                    "message": "Successfully updated user",
                    "id": f"{id}",
                }
            ),
            status=200,
            mimetype="application/json",
        )
    except Exception as e:
        print(f"Error in creating user : {e}")
        return Response(
            response=json.dumps({"message": f"Error in deleting user : {e}"}),
            status=400,
            mimetype="application/json",
        )


if __name__ == "__main__":
    app.run(debug=True)
