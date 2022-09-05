
from flask import render_template ,request,redirect,abort
from flask import Blueprint
from iti.models import Book,db,Author
from werkzeug.utils import secure_filename

books_blueprint=Blueprint("books", __name__,url_prefix="/")


@books_blueprint.route("/")
def index():
    books= Book.query.all()
    authors=Author.query.all()
    return render_template("index.html",books=books,authors=authors)

@books_blueprint.route("/book/<int:book_id>")
def book_details(book_id):
    book= Book.query.get_or_404(book_id)
    author=Author.query.get_or_404(book.author_id)
    
    return render_template("details.html",book=book,author=author)


@books_blueprint.route('/book/create' , methods = ['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('createpage.html')
 
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']
        appropriate=request.form['appropriate']
        author_id=request.form['author_id']
        f = request.files['file']
        f.save(secure_filename(f.filename))
        book = Book(name=name, description=description, price = price,appropriate=appropriate,author_id=author_id,image=f.filename)
        db.session.add(book)
        db.session.commit()
        return redirect('/')



@books_blueprint.route('/book/<int:id>/update',methods = ['GET','POST'])
def update(id):
    book = Book.query.filter_by(id=id).first()
    if request.method == 'POST':
        if book:
            db.session.delete(book)
            db.session.commit()
 
            name = request.form['name']
            description = request.form['description']
            price = request.form['price']
            appropriate= request.form['appropriate']
            author_id=request.form['author_id']
            f = request.files['file']
            f.save(f.filename)
            book = Book(name=name, description=description, price = price,appropriate=appropriate,author_id=author_id,image=f.filename)
    
            db.session.add(book)
            db.session.commit()
            return redirect(f'/')

 
    return render_template('update.html', book=book)


@books_blueprint.route('/book/<int:id>/delete',methods = ['GET','POST'])
def delete(id):
    book = Book.query.filter_by(id=id).first()
    if request.method == 'POST':
        if book:
            db.session.delete(book)
            db.session.commit()
 
            return redirect(f'/')
        
        abort(404)
    return render_template('delete.html')