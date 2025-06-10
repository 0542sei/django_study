from flask import Flask, url_for

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World"

@app.route("/user/<username>")
def show_user_profile(username):
    return f"사용자 이름: {username}"

@app.route('/post/<int:post_id>/<slug>')
def show_post(post_id, slug):
    return f"Showing post with ID : {post_id} - Slug:{slug}"

if __name__ == '__main__':
    with app.test_request_context():
        home_url = url_for("hello_world")
        profile_url = url_for("show_user_profile", username="antony")
        post_url = url_for("show_post", post_id=456, slug="flask-intro")

        print("Generated URLs:")
        print("Home URL:", home_url)
        print("Author profile URL:", profile_url)
        print("Post URL:", post_url)
