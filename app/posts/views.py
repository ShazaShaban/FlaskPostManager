from app.posts import posts_blueprint
from app.models import Post, Category,db
from flask import request, render_template, redirect, url_for
import os 
from werkzeug.utils import secure_filename

@posts_blueprint.route('', endpoint = 'index')
def index():
  posts = Post.get_all_objects()
  categories = Category.get_all_objects()

  return render_template('posts/index.html', posts=posts, categories=categories)

@posts_blueprint.route('/create', methods=['GET', 'POST'],endpoint = 'create')
def create():
    categories = Category.get_all_objects()
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        body = request.form['body']
        image = request.files['image']
        category_id = request.form['category_id']

        # Check if the image field is empty
        if image.filename == '':
            return render_template('posts/create.html', error='Image field is required.')

        # Save the uploaded image to a folder (create the folder if it doesn't exist)
        upload_folder = 'app/static/posts/images'  # Use a relative path
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)

        # Secure the filename to prevent any security issues
        filename = secure_filename(image.filename)
        image.save(os.path.join(upload_folder, filename))

        # Create a new Post entry with the form data
        post = Post(name=name, body=body, image=filename, category_id=category_id)
        db.session.add(post)
        db.session.commit()

        return redirect(url_for('posts.index'))

    return render_template('posts/create.html', categories=categories)


@posts_blueprint.route('<int:id>', endpoint='show')
def show(id):
    post = Post.get_specific_post(id)
    return  render_template('posts/show.html', post=post)

@posts_blueprint.route('<int:id>/delete', endpoint='delete')
def delete(id):
    post=Post.query.get_or_404(id)
    if post:
        db.session.delete(post)
        db.session.commit()
        return redirect(url_for('posts.index'))
    else:
        return '<h1> Object not found </h1>', 404


@posts_blueprint.route('<int:id>/edit', methods=['GET', 'POST'],endpoint='edit')
def edit(id):
    post = Post.query.get_or_404(id)
    categories = Category.get_all_objects()
    if post:
        if request.method == 'POST':
            # Check if the name field is present in the request form
            if 'name' not in request.form:
                return render_template('blogs/edit.html', error='The name field is required.', post=post)

            # Check if the field name is correct
            if request.form['name'].strip() == '':
                return render_template('blogs/edit.html', error='The name field cannot be empty.', post=post)

            # Get the name and body values
            name = request.form['name']
            body = request.form['body']
            category_id = request.form['category_id']

            # Handle image upload
            image = request.files['image']
            if image.filename:
                # Save the uploaded image to a folder (create the folder if it doesn't exist)
                upload_folder = 'static/posts/images'
                if not os.path.exists(upload_folder):
                    os.makedirs(upload_folder)

                # Secure the filename to prevent any security issues
                filename = secure_filename(image.filename)
                image.save(os.path.join(upload_folder, filename))

                # Update the blog object with the new image filename
                post.image = filename

            # Update the blog object
            post.name = name
            post.body = body
            post.category_id = category_id

            db.session.commit()

            return redirect(url_for('posts.index'))

        return render_template('posts/edit.html', post=post, categories=categories)

    return '<h1> Object not found </h1>', 404