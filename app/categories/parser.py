from flask_restful import reqparse

category_parser = reqparse.RequestParser()

category_parser.add_argument('name', type=str, required=True,
                            help='Category is required')