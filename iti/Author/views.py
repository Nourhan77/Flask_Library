from flask import render_template ,request,redirect,abort
from flask import Blueprint
from iti.models import Author,db



authors_blueprint=Blueprint("authors", __name__,url_prefix="/")

@authors_blueprint.route('/author/create' , methods = ['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('authorcreatepage.html')
 
    if request.method == 'POST':
        name = request.form['name']
        author = Author(name=name)
        db.session.add(author)
        db.session.commit()
        return redirect('/')


@authors_blueprint.route("/author/<int:author_id>")
def author_details(author_id):
    author= Author.query.get_or_404(author_id)
    return render_template("author_details.html",author=author)
