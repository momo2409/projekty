version: 1.0.0
author: Šimon Matejička
Mycroservice RESTful API in python

operations:
	Create
		adding new posts
	Read
		showwing posts by id or userid
		by id: show post with given id
		by userid: show every post that was added by given userid
	Update
		able to update userid, title, body
		to update it needs to hawe id of title whitch will be updated a then you have to describe new verision of the post(updated version)
	Delete
		delete post by it's id

how to set up and test API:

1. open a terminal a run tihs serie of commands in folder master:
	1.1: Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted
	1.2: .\\.venv\Scripts\activate
	1.3: $env:FLASK_APP="app.py"
	1.4: flask run
now is a local host server with rest api is working

2. for testing i used Postman. Choose Method you want to test and tipe this endpoints:
	2.1 GET:    /posts 		   -get all posts in database
		    /posts/id/<id> 	   -get post with defined id
		    /posts/userid/<userid> -get all posts in database with defined userid
	2.2 POST:   /posts		   -add new post
	2.3 PUT:    /posts/update	   -update everything in post with defined id
	2.4 DELETE: /posts/id/<id>	   -delete post with defined id