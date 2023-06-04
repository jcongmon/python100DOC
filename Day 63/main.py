from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///bookshelf.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), unique=True, nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'


db.create_all()

# new_book = Book(title="Harry Potter", author="J. K. Rowling", rating=9.3)
# db.session.add(new_book)
# db.session.commit()

# all_books = []

# db = sqlite3.connect('bookshelf.db')
# cursor = db.cursor()

# try:
#     cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title VARCHAR(250) NOT NULL UNIQUE,"
#                    "author VARCHAR(250) NOT NULL UNIQUE, rating FLOAT NOT NULL)")
# except sqlite3.OperationalError:
#     # db already exists
#     pass
#
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()


@app.route('/')
def home():
    return render_template("index.html", books=Book)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        data = request.form
        # new_book = {
        #     'name': data['name'],
        #     'author': data['author'],
        #     'rating': data['rating'],
        # }
        # all_books.append(new_book)
        new_book = Book(title=data['name'], author=data['author'], rating=data['rating'])
        db.session.add(new_book)
        db.session.commit()
        return render_template("index.html", books=Book)
    return render_template("add.html")


@app.route("/edit", methods=['GET', 'POST'])
def edit():
    if request.method == 'POST':
        update_book = Book.query.filter_by(id=request.form['id']).first()
        update_book.rating = request.form['rating']
        db.session.commit()
        return render_template("index.html", books=Book)
    book_id = request.args.get('id')
    current_book = Book.query.filter_by(id=book_id).first()
    return render_template("edit.html", book=current_book)


@app.route("/delete")
def delete():
    book_id = request.args.get('id')
    current_book = Book.query.get(book_id)
    db.session.delete(current_book)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
