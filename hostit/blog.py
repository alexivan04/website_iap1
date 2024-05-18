import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, current_app
)

from hostit.db import get_db
import os
import imghdr
import uuid
from flask import request, session, send_from_directory
from werkzeug.utils import secure_filename

bp = Blueprint('blog', __name__, url_prefix='/blog')

@bp.route('/about_me', methods=['GET'])
def about_me():
    return render_template('blog/about_me.html')

@bp.route('/post_image', methods=('GET', 'POST'))
def post_image():
    if request.method == 'POST':
        error = None
        image = request.files['image']
        user_id = session.get('user_id')
        filename = secure_filename(image.filename)
        
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in current_app.config[
            "UPLOAD_EXTENSIONS"
        ] or file_ext != validate_image(image.stream):
            error = "Invalid image extension"
            
        else:
            # check if filename exists, if so, generate a new filename
            while os.path.exists(os.path.join(current_app.config["UPLOAD_PATH"], filename)):
                filename = str(uuid.uuid4()) + filename
            
            print(filename)
            db = get_db()
            error = None

            if not image:
                error = 'Image is required.'

            if error is None:
                try:
                    db.execute(
                        "INSERT INTO image (user_id, image) VALUES (?, ?)",
                        (user_id, filename),
                    )
                    db.commit()
                except db.IntegrityError:
                    error = f"Error posting image"
                else:
                    flash("Image posted successfully")
                    image.save(os.path.join(current_app.config["UPLOAD_PATH"], filename))
                    return redirect(url_for("blog.post_image"))
                
        flash(error)
    return render_template('blog/post_image.html')

def validate_image(stream):
    header = stream.read(512)
    stream.seek(0)
    format = imghdr.what(None, header)
    if not format:
        return None
    return "." + (format if format != "jpeg" else "jpg")