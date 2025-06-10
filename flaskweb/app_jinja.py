from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = "Alice"
    items = ["Apple", "Banana", "Cherry"]
    user = {'username': 'bob123', 'email': 'bob@example.com'}
    return render_template('index.html', user_name=name, item_list=items, user_info=user)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
