from flask_restful import Resource, fields, abort, marshal_with
from flask import make_response
from app.models import db, Category
from app.categories.parser import category_parser
from app.categories.serializers import category_serializer


class CategoryList(Resource):
    @marshal_with(category_serializer)
    def get(self):
        categories = Category.get_all_objects()
        return categories, 200
    
    @marshal_with(category_serializer)
    def post(self):
        category_args = category_parser.parse_args()
        category = Category.create_category(category_args)

        return category, 201
    

class CategoryResource(Resource):
    @marshal_with(category_serializer)
    def get(self, cat_id):
        category = Category.get_specific_category(cat_id)
        return category, 200

    @marshal_with(category_serializer)
    def put(self, cat_id):
        category = Category.get_specific_category(cat_id)
        if category:
            category_args = category_parser.parse_args()
            category.name = category_args['name']
            db.session.add([category])
            db.session.commit()

            return  category, 200

        abort(404, message='Category object not found')

    @marshal_with(category_serializer)
    def delete(self, cat_id):
        category = Category.get_specific_category(cat_id)
        if category:
            db.session.delete(category)
            db.session.commit()
            response = make_response("deleted", 204)
            return  response

        abort(404)