from flask import Flask
from app.book import book_blueprint,landing_blueprint
from app.models import Book,db
from flask import render_template,request,redirect,url_for
from app.book.forms import PostForm,EditForm
from werkzeug.utils import secure_filename
import os


@landing_blueprint.route("",endpoint="landing")
def landing():
    books=Book.query.all()
    return render_template("landing.html",books=books)

@book_blueprint.route("<int:id>/show",endpoint="show")
def show(id):
    book = db.get_or_404(Book, id)
    return render_template ("show.html",book=book)

@book_blueprint.route("<int:id>/delete",endpoint="delete")
def delete(id):
    book = db.get_or_404(Book, id)
    db.session.delete(book)
    db.session.commit()
    return redirect (url_for("landing.landing"))

@book_blueprint.route("/form/add",endpoint="add",methods=['GET','POST'])
def add():
    form=PostForm()
    if request.method=="POST":
        if form.validate_on_submit():
                request.files.get("cover_photo")
                image=form.image.data
                image_name =secure_filename(image.filename)
                image.save(os.path.join('static/images/', image_name))
                data=dict(request.form)
                del data['csrf_token']
                del data['submit']
                data["cover_photo"]=image_name
                book=Book(**data)
                db.session.add(book)
                db.session.commit()
                return redirect(url_for("landing.landing"))
            
        
    return render_template("add.html",form=form)


@book_blueprint.route("<int:id>/form/edit",endpoint="edit",methods=['GET','POST'])
def edit(id):
    book=db.get_or_404(Book,id)
    form=EditForm(obj=book)
    if request.method=="POST":
        if form.validate_on_submit():
                if request.files.get("cover_photo"):
                    image=form.image.data
                    image_name =secure_filename(image.filename)
                    image.save(os.path.join('static/images/', image_name))
                    book.cover_photo=image_name
                else:
                    book.cover_photo=book.cover_photo
                book.title=form.title.data
                book.number_of_pages=form.number_of_pages.data
                book.description=form.description.data
                db.session.commit()
                return redirect(url_for("landing.landing"))
            
        
    return render_template("edit.html",form=form)


