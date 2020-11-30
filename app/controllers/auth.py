from app import app
from functools import wraps
from flask import request, jsonify
import jwt
import datetime
from app.database import database
from app.models import User
from sqlalchemy.sql import select
app.config['SECRET_KEY'] = "!Flask#API@"


def check_for_token(func):
	@wraps(func)
	def wrapped(*args, **kwargs):
		token = request.headers.get('token')
		if not token:
			return jsonify({'message':'Missing token'}), 403
		try:
			data = jwt.decode(token, app.config['SECRET_KEY'])
		except:
			return jsonify({'message': 'Invalid token'}), 403
		return func(*args, **kwargs)
	return wrapped

@app.route('/auth')
@check_for_token
def authorised():
	return "Just for token guys"

@app.route('/login', methods=['POST'])
def login():
	result = database.con.execute(select([User.users.c.mail, User.users.c.password]).where(User.users.c.mail==request.json['mail']))
	if(result._saved_cursor.rowcount==1):
		print("find user")
		row = result.fetchone()
		if row['password']==request.json['password']:
			token = jwt.encode({
				'user':request.json['mail'],
				'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=6000)
			},
			app.config['SECRET_KEY'])
			return jsonify({'token' : token.decode('utf-8')})
		else:
			return "{ 'message': 'Not found user or password'}"
	else:
		return "{ 'message': 'Not found user or password'}"
		