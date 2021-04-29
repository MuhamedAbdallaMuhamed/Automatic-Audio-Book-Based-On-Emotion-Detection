from flask import Flask, jsonify, request, Blueprint, Response

from core.entities import *
from core.use_cases import *
from core.entities.exception import *
import json

# initializing FLASK
app = Flask(__name__)

# initializing api
api_bp = Blueprint('api', __name__)

app.register_blueprint(api_bp)


def hash_book():
    return "hahahahaha"


# Add book
@app.route('/book/add', methods=['POST'])
def AddBook():
    model = request.get_json()
    book_hash = hash_book()
    add_book(
        book_path=model["path"],
        sentence_features=model["sentence_features"],
        book_hash=book_hash,
        name=model["name"]
    )
    book = get_book_by_book_hash(book_hash=book_hash)
    return jsonify(book.__dict__)


@app.route('/book/id/<string:id>', methods=['GET'])
def GetBookById(id):
    book = get_book_by_id(id)
    return book.__dict__


@app.route('/book/hash/<string:hash>', methods=['GET'])
def GetBookByHash(hash):
    book = get_book_by_book_hash(hash)
    return book.__dict__


# Edit Book
@app.route('/book/update', methods=['POST'])
def UpdateBook():
    model = request.get_json()
    update_book(
        id=model["id"],
        book_path=model["path"],
        sentence_features=model["sentence_features"],
        book_hash=model["hash"],
        name=model["name"]
    )
    book = get_book_by_id(model["id"])
    return book.__dict__


@app.route('/books/Parse')
def parse_book():
    return jsonify()


# Add user book
@app.route('/book/add-user-book', methods=['POST'])
def AddUserBook():
    model = request.get_json()
    add_user_book(
        book_id=model["book_id"],
        user_id=model["user_id"],
        title=model["title"],
    )
    return jsonify(True)


@app.route('/book/user-book/<string:id>', methods=['GET'])
def GetUserBookById(id):
    user_book = get_user_book_by_id(id)
    return user_book.__dict__


@app.route('/book/delete-user-book/<string:id>', methods=['POST'])
def DeleteUserBook(id):
    status = delete_user_book(id)
    return Response(status)
