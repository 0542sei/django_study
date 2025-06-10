from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/user/<username>")
def show_user_profile(username):
    return render_template("profile.html", username=username)

if __name__ == '__main__':
    app.run()
