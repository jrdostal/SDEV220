from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

db = SQLAlchemy(app)

@app.route('/')
def index():
    return 'Hello'

class Book(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    book_name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))
    author = db.Column(db.String(120))
    publisher = db.Column(db.String(120))

    def __repr__(self) -> str:
        return f"{self.book_name} - {self.description}"
    
@app.route('/books')
def get_books():
    books = Book.query.all()
    output =[]

    for book in books:
        book_data = {'name': book.book_name, "description": book.description}
        output.append(book_data)
    return {"books": output}

    return Books

@app.route('/books/<id>')
def get_single_book(id):
    book = Book.query.get_or_404(id)
    return {'name': book.book_name, "description": book.description}
   