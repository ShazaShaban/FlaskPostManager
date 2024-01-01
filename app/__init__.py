from flask import Flask
from flask_migrate import Migrate
from app.models import db, Category
from app.config import projectConfig as AppConfig
from flask import render_template
from flask_restful import Api
from app.posts.api_views import PostList, PostResource
from app.categories.api_views import CategoryList, CategoryResource

def create_app(config_name='dev'):
    app = Flask(__name__)
    app.static_folder = 'static'
   
    current_config = AppConfig[config_name]  ##config class
    app.config['SQLALCHEMY_DATABASE_URI'] = current_config.SQLALCHEMY_DATABASE_URI  #7dd sh8alen b anhy config
    app.config['SQLALCHEMY_DATABASE_URI'] = current_config
    app.config.from_object(current_config)
    db.init_app(app)

    api = Api(app)

    migrate = Migrate(app, db, render_as_batch=True)

    api.add_resource(PostList, '/api/posts')
    api.add_resource(PostResource, '/api/posts/<int:post_id>')
    api.add_resource(CategoryList, '/api/categories')
    api.add_resource(CategoryResource, '/api/categories/<int:cat_id>')


    # register blueprint in the application
    from app.posts import posts_blueprint
    app.register_blueprint(posts_blueprint)

    from app.categories import categories_blueprint
    app.register_blueprint(categories_blueprint)

    @app.errorhandler(404)
    def page_not_found(error):
        print(error)
        return  render_template('errors/page_not_found.html')

    return app


# Error Page
