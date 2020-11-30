from app import app
from flask import request, jsonify, abort
from sqlalchemy.sql import select, update
from app.database import database
from app.models import User
from  app.controllers import auth
import json


# Get list of all users
@app.route('/users/', methods=['GET'])
@auth.check_for_token
def getAllUsers():
    try:
        return jsonify(get_paginated_list(
		User.users, 
		'/users/', 
		start=request.args.get('start', 1), 
		limit=request.args.get('limit', 20)
	))
    except Exception as err:
        return jsonify({ 
                'status':'error',
                'message': err
            }) 


# Get user by id
@app.route('/users/<IdUser>', methods=['GET'])
@auth.check_for_token
def getUserByUsername(IdUser):
    try:
        result = database.con.execute(select([User.users.c.name,User.users.c.mail]).where(User.users.c.id==IdUser))
        return jsonify([dict(r) for r in result]) # Print result like json
    except Exception as err:
        return jsonify({ 
                'status':'error',
                'message': str(err)
            }) 



# Insert user
@app.route('/users', methods=['POST'])
def insertUser():
    try:
        name_ = request.json['name']
        mail_ = request.json['mail']
        password_ = request.json['password']
        result = database.con.execute(User.users.insert().values(name=name_, mail=mail_, password=password_))
        return jsonify({ 
            'status':'success',
            'message':'User created with success.'
        }) 
    except Exception as err:
        return jsonify({ 
                'status':'error',
                'message': str(err)
            }) 

# Update user
@app.route('/users/<IdUser>', methods=['PUT'])
@auth.check_for_token
def updateUser(IdUser):
    try:
        name_ = request.json['name']
        mail_ = request.json['mail']
        stmt = User.users.update().\
                        where(User.users.c.id==IdUser).\
                        values(name=name_, mail=mail_)
        result = database.con.execute( stmt )   #(User.users.update().values(name=name_).where(User.users.c.mail==username))
        return jsonify({ 
            'status':'success',
            'message':'User updated with success.'
        })
    except Exception as err:
        return jsonify({ 
                'status':'error',
                'message': str(err)
            }) 

# Delete user
@app.route('/users/<IdUser>', methods=['DELETE'])
@auth.check_for_token
def deleteUser(IdUser):
    try:
        result = database.con.execute(User.users.delete().where(User.users.c.id==IdUser)) 
        return jsonify({ 
            'status':'success',
            'message':'User deleted with success.'
        }) 
    except Exception as err:
        return jsonify({ 
                'status':'error',
                'message': str(err)
            }) 

# Pagination
def get_paginated_list(klass, url, start, limit):
    # check if page exists
    results = database.con.execute(select([User.users.c.id, User.users.c.name,User.users.c.mail]))
    count = results._saved_cursor.rowcount
    if (count < start or count == 0):
        return "Nenhum registro encontrado"
    # make response
    obj = {}
    obj['start'] = start
    obj['limit'] = limit
    obj['count'] = count
    # make URLs
    # make previous url
    if start == 1:
        obj['previous'] = ''
    else:
        start_copy = max(1, start - limit)
        limit_copy = start - 1
        obj['previous'] = url + '?start=%d&limit=%d' % (start_copy, limit_copy)
    # make next url
    if start + limit > count:
        obj['next'] = ''
    else:
        start_copy = start + limit
        obj['next'] = url + '?start=%d&limit=%d' % (start_copy, limit)
    # finally extract result according to bounds
    d, a = {}, []
    for rowproxy in results:
        # rowproxy.items() returns an array like [(key0, value0), (key1, value1)]
        for column, value in rowproxy.items():
            # build up the dictionary
            d = {**d, **{column: value}}
        a.append(d) # a = query results in dict format
    obj['results'] = a[(start - 1):(start - 1 + limit)]
    return obj['results']