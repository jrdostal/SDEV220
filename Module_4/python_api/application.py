from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite+pysqlite:///C:\\Users\\dosta\\OneDrive\\Documentos\\Homework\\SDEV220\\Module_4\\python_api\\instance\\data.db'
engine = create_engine('sqlite+pysqlite:///C:\\Users\\dosta\\OneDrive\\Documentos\\Homework\\SDEV220\\Module_4\\python_api\\instance\\data.db')
Session = sessionmaker(bind=engine)

db = SQLAlchemy(app)

book_author = Table('book_author', Base.metadata,
    Column('book_id', Integer, ForeignKey('books.id')),
    Column('author_id', Integer, ForeignKey('authors.id'))
)

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    book_name = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=False)
    publisher = Column(String, nullable=False)
    authors = relationship("Author", secondary=book_author, back_populates="books", uselist=True)

    def __repr__(self):
        return f"{self.book_name} - {self.description}"

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    books = relationship("Book", secondary=book_author, back_populates="authors", uselist=True)

    def __repr__(self):
        return f"{self.name} - {self.books}"

@app.route('/')
def index():
    return 'Hello'

@app.route('/books', methods=['GET'])
def get_all_books():
    session = Session()
    books = session.query(Book).all()
    return jsonify([{'id': book.id, 'title': book.book_name, 'description': book.description, 'authors': book.authors, "publisher": book.publisher} for book in books])

@app.route('/books', methods=['POST'])
def add_book():
    session = Session()
    data = request.get_json()
    new_book = Book(id=data['id'], book_name=data['book_name'], description=data['description'], authors=data['authors'],publisher=data['publisher'])
    session.add(new_book)
    session.commit()
    return jsonify({'id': new_book.id, "book_name": new_book.book_name, "description":new_book.description, "authors": new_book.authors, "publisher": new_book.publisher}), 201

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    session = Session()
    book = session.query(Book).get(book_id)
    if book:
        return jsonify({'id': book.id, 'title': book.book_name, 'description': book.description, 'authors': book.authors, "publisher": book.publisher})
    else:
        return jsonify({'error': 'Book not found'}), 404

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    session = Session()
    book = session.query(Book).get(book_id)
    if book:
        session.delete(book)
        session.commit()
        return jsonify({'message': 'Book was deleted'})
    else:
        return jsonify({'error': 'Book not found'}), 404

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    app.run(debug=True)
   