from flask import Flask, request

app = Flask(__name__)

@app.route("/",methods=["GET"])
def index():
    return "This is the home page"

@app.route("/authors", methods=["GET","POST"]) 
def authors():
    if request.method=="GET":
        return "Get all authors"
    elif request.method=="POST":
        return "Create a new author"
    #get,post 외에 들어올 수 있기에 else같은걸 넣어서 보안 위험에 대비해야함
    else:
        return None
    
@app.route('/authors/<int:author_id>', methods=["GET","PUT","DELETE"])
def author(author_id):
    if request.method == 'GET':
        return f"Get author with ID: {author_id}"
    elif request.method == 'PUT':
        # Update author with ID: author_id
        return f"Update author with ID: {author_id}"
    elif request.method == 'DELETE':
        # Delete author with ID: author_id
        return f"Delete user with ID: {author_id}"
    else:
        return None

if __name__ == '__main__':
    app.run()
