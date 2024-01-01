from flask_restful import fields


category_serializer = {
    "id": fields.Integer,
    "name": fields.String
}