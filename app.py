from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        posts = Post.query.order_by(Post.due).all()  # (締め切り順に)
        return render_template("index.html", posts=posts)

    else:
        title = request.form.get("title")
        detail = request.form.get("detail")
        due = request.form.get("due")

        due = datetime.strptime(due, "%Y-%m-%d")
        new_post = Post(title=title, detail=detail, due=due)

        db.session.add(new_post)
        db.session.commit()
        return redirect("/")


@app.route("/test")
def test():
    return render_template("test.html")


@app.route("/create")
def create():
    return render_template("create.html")


if __name__ == "__main__":
    app.run(debug=True)
