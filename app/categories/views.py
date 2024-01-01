from app.categories import categories_blueprint
from flask import request, render_template, redirect, url_for
from app.models import Category, db
import os
from werkzeug.utils import secure_filename



@categories_blueprint.route('/index', endpoint='list')

def index():
    categories  = Category.get_all_objects()
    return render_template('layouts/base.html', categories=categories)
# 



@categories_blueprint.route('/create', endpoint='create',methods = ['GET', 'POST'])

def create():

    categories = Category.get_all_objects()

    if request.method == 'POST':
        # Get form data
        name = request.form['name']

        
        # Create a new Blog entry with the form data
        category = Category(name=name)
        db.session.add(category)
        db.session.commit()

        return redirect(url_for('posts.index'))

    return render_template('categories/create.html', categories=categories)

@categories_blueprint.route('<int:id>', endpoint='show')
def show(id):
    category = Category.get_specific_category(id)
    return  render_template('categories/show.html', category=category)

@categories_blueprint.route('<int:id>/delete', endpoint='delete')
def delete(id):
    category=Category.query.get_or_404(id)
    if category:
        db.session.delete(category)
        db.session.commit()
        return redirect(url_for('posts.index'))
    else:
        return '<h1> Object not found </h1>', 404
    

@categories_blueprint.route('<int:id>/edit', methods=['GET', 'POST'],endpoint='edit')
def edit(id):
    category = Category.query.get_or_404(id)
    if category:
        if request.method == 'POST':
            # Check if the name field is present in the request form
            if 'name' not in request.form:
                return render_template('categpries/edit.html', error='The name field is required.', category=category)

            # Check if the field name is correct
            if request.form['name'].strip() == '':
                return render_template('blogs/edit.html', error='The name field cannot be empty.', category=category)

            # Get the name and body values
            name = request.form['name']
            
            
            # Update the blog object
            category.name = name
            
            db.session.commit()

            return redirect(url_for('posts.index'))

        return render_template('categories/edit.html', category=category)

    return '<h1> Object not found </h1>', 404
