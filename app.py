from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/new")
def new():
    return render_template("new.html")


@app.route("/show", methods=["GET", "POST"])
def show():
    if request.method == "GET":
        return render_template("show.html")
    else:
        passage = request.form.get("passage")
        return render_template("show.html", passage3=passage)


@app.route("/test")
def test():
    return render_template("test.html")


if __name__ == "__main__":
    app.run(debug=True)
