from flask_restful import fields
from app.categories.serializers import category_serializer

post_serializer = {
  "id": fields.Integer,
  "name": fields.String,
  "body": fields.String,
  "image": fields.String,
  "category_id": fields.Integer,
  "category_name": fields.Nested(category_serializer)
}