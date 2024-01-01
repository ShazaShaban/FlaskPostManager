from flask_restful import Resource, fields, marshal_with, abort
from flask import  make_response
from app.models import Post, Category, db
from app.posts.parser import  post_parser
from app.posts.serializers import post_serializer
## api --> receive data from form


## seriliaze data


## crud operations

class PostList(Resource):
    @marshal_with(post_serializer)
    def get(self):
        posts = Post.get_all_objects()
        return posts,200

    @marshal_with(post_serializer)
    def post(self):
        # pass
        # get data from form >
        # parsing form data --> x-application
        post_args = post_parser.parse_args()
        print(post_args) # dict ---> parsing
        post = Post.create_post(post_args)
        return post, 201

  
        ## saving , return with result



class PostResource(Resource):
    @marshal_with(post_serializer)
    def get(self, post_id):
        post = Post.get_specific_post(post_id)
        return post, 200

    @marshal_with(post_serializer)
    def put(self, post_id):
        post = Post.get_specific_post(post_id)
        if post:
            post_args = post_parser.parse_args()
            post.name = post_args['name']
            post.body = post_args['body']
            post.image = post_args['image']
            post.category_id = post_args['category_id']
            db.session.add(post)
            db.session.commit()
            return post, 200
        abort(404, message='Post Not Found')

    @marshal_with(post_serializer)
    def delete(self, post_id):
        post = Post.get_specific_post(post_id)
        if post:
            db.session.delete(post)
            db.session.commit()
            response = make_response("deleted", 204)
            return  response

        abort(404)