#!/usr/bin/env python3

"""
Flask simple REST API exercice
==============================
2022 Evgueni Antonov
"""

import json

# import requests

# from markupsafe import escape
from flask import Flask, abort, request

# from flask import url_for
# from flask import render_template


# Example data
people = {
    "joe": {"name1": "John", "name2": "Doe", "age": 43},
    "jenny": {"name1": "Jenny", "name2": "Simpson", "age": 24},
}


app = Flask(__name__)


@app.get("/")
def homepage():
    """Prints help"""

    # return f"<h1>here goes nothing</h1>"
    # return render_template('index.html') # Jinja2 template
    return "USAGE: GET: <SHORTNAME> ; POST: short_name=<SHORTNAME> name1=<NAME1> name2=<NAME2> age=<AGE> ; DELETE: <SHORTNAME>"


@app.get("/<short_name>")
def get_person(short_name):
    """Gets person information or list of all short names, if shortname='all'"""

    if short_name not in people and short_name != "all":
        abort(404)

    if short_name == "all":
        return json.dumps(list(people.keys()), indent=4)

    return json.dumps(people[short_name], indent=4)


@app.post("/")
def insert_person():
    """Inserts a new person"""

    required_fields = ["short_name", "name1", "name2", "age"]
    new_person = request.get_json()

    for field in required_fields:
        if field not in new_person:
            abort(404)

    short_name = new_person["short_name"]
    del new_person["short_name"]

    if short_name in people:
        abort(401)

    people[short_name] = new_person
    return json.dumps(new_person, indent=4)


@app.delete("/<short_name>")
def delete_person(short_name):
    """Deletes a person"""

    if short_name not in people:
        abort(404)

    deleted_person = people[short_name]
    del people[short_name]

    return json.dumps(deleted_person, indent=4)


if __name__ == "__main__":
    app.run()
