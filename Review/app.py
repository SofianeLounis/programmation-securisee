#!/usr/bin/env python3
"""avis/app.py
Develop the power of Flask and Jinja by creating HTML templates,
expending those templates, and pass variable to create dynamic content.
"""

import flask
from flask import render_template, request # import the flask library

app = flask.Flask(__name__)  # instantiate a minimal webserver


@app.route("/")
def index():
    # Render the form page
    return flask.render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    # Get the user's opinion from the form submission
    opinion = request.form["opinion"]

    # Render the page that displays the user's opinion
    return flask.render_template("submit.html", opinion=opinion)

if __name__ == '__main__':  # consider this line as the main
    app.run('0.0.0.0', 8080, debug=True)  # start web server in debug mode on port 8080
