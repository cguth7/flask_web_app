from flask import Blueprint, render_template, request, flash, url_for, redirect, current_app, session
from flask_login import login_required, current_user
from .models import Note, User, Image
from werkzeug.utils import secure_filename
from . import db
import os

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

views = Blueprint('views', __name__)

@views.route('/',methods=["GET","POST"])
@login_required
def home():
    if request.method == "POST":
        data = request.form.get("note")

        if len(data) < 1: 
            flash("You must enter characters to add a note", category="error")
        else:
            new_note = Note(data=data, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash("Note added!", category="success")

    return render_template("home.html", user=current_user)

@views.route("/userinfo")
@login_required
def userinfo():
    users = User.query.all()
    return render_template("userinfo.html", users=users, user=current_user)

@views.route("/photoform", methods=["GET", "POST"])
@login_required
def photoform():
    if request.method == "POST":
        print("hi")
        pic = request.files["uploaded-file"]
        img_filename = secure_filename(pic.filename)
        pic.save(os.path.join(current_app.config['UPLOAD_FOLDER'], pic.filename))
        session['filename'] = os.path.join(current_app.config['UPLOAD_FOLDER'], )
        return redirect(url_for("views.showphoto"))

        


        
    return render_template("photoform.html", user=current_user)


@views.route('/show_image')
def showphoto():
    print("hi")
    file_name = session.get('filename', None)
    print(file_name)
    return render_template("showimage.html", file_name=file_name, user=current_user)


