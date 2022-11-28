from flask import Flask
from flask import render_template
import db

# FIXME: remove this variable when the db queries are in place.

messages = [
    {
        "id": 0,
        "title": "first item",
        "details": "lorem ipsum"
    },
    {
        "id": 1,
        "title": "second item",
        "details": "dolor sit"
    },
    {
        "id": 2,
        "title": "third item",
        "details": "amet consecteur",
    }
]


# FIXME: remove this function when the db queries are in place.


def findItemById(item_id=None):
    global messages

    for item in messages:
        if item["id"] == item_id:
            return item

    # return error if the item wasn't found.
    return {
        "id": -1,
        "title": "error",
        "details": "failed to find item with given id."
    }


app = Flask(__name__)
db.init_app(app)


@app.route("/")
def index():
    # TODO: replace this with a database query.
    global messages
    return render_template("main.html", items=messages)


@app.route("/details/<int:item_id>")
def details(item_id):
    # TODO: replace this with a database query.
    item = findItemById(item_id)
    return render_template("details.html", item=item)
