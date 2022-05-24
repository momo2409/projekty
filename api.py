from flask import Flask
from flask_sqlalchemy import SQLAlchemy, request
import requests
import json

app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
   
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer,)
    title = db.Column(db.String(80))
    body = db.Column(db.String(200))
    
    def __repr__(self):
        return f"{self.id}:{self.userid}:{self.title}:{self.body}"


@app.route('/posts')
def get_posts():
    posts = Post.query.all()
    output = []
    
    for post in posts:
        post_data = {'id':post.id, 'userid':post.userid, 'title':post.title, 'body':post.body}
        output.append(post_data)
    
    return {"posts": output}


@app.route('/posts/id/<id>')
def get_post_id(id):
    post = Post.query.get(id)
    
    if post == None:
        return {"message": "post not found"}
    else:
        return {"title": post.title, "body": post.body}


@app.route('/posts/userid/<userid>')
def get_post_userid(userid):
    posts = Post.query.all()
    output = []

    for post in posts:
        post_data = {
            'id':post.id,
            'userid':post.userid,
            'title':post.title,
            'body':post.body
        }
        if int(userid) == post_data['userid']:
            output.append(post_data)
    if output == []:
        return {"message": "post for this user was not found"}
    else:
        return {"posts": output}


@app.route('/posts', methods=['POST'])
def add_post():
    post = Post(
                userid=request.json['userid'],
                title=request.json['title'],
                body=request.json['body']
            )
    db.session.add(post)
    db.session.commit()
    return {"message": "post added successfully"}


@app.route('/posts/update', methods=['PUT'])
def update_post():
    post = Post(
                id = request.json['id'],
                userid = request.json['userid'],
                title = request.json['title'],
                body = request.json['body']
            )
    old_post = Post.query.get(post.id)
    db.session.delete(old_post)
    db.session.add(post)
    db.session.commit()
    return {"message": "post updated successfully"}


@app.route('/posts/id/<id>', methods=['DELETE'])
def delete_post(id):
    post = Post.query.get(id)

    if post == None:
        return {"error": "post not found or already deleted"}
    else:
        db.session.delete(post)
        db.session.commit()
        return {"message": "post deleted successfully"}