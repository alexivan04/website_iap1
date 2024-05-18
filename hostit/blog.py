import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from hostit.db import get_db

bp = Blueprint('blog', __name__, url_prefix='/blog')

@bp.route('/about_me', methods=['GET'])
def about_me():
    return render_template('blog/about_me.html')

@bp.route('/post_image', methods=('GET', 'POST'))
def post_image():
    if request.method == 'POST':
        image = request.files['image']
        print(image)
        db = get_db()
        error = None

        if not image:
            error = 'Image is required.'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO image (image) VALUES (?)",
                    (image.read(),),
                )
                db.commit()
            except db.IntegrityError:
                error = f"Image is already posted."
            else:
                return redirect(url_for("blog.post_image"))

        flash(error)

    return render_template('blog/post_image.html')