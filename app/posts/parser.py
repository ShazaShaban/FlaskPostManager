from flask_restful import  reqparse

post_parser = reqparse.RequestParser()

post_parser.add_argument('name', type=str,required=True,
                            help='Post is required')

post_parser.add_argument('body', type=str)

post_parser.add_argument('image', type=str)

post_parser.add_argument('category_id', type=int)