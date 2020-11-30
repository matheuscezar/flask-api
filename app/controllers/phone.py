from app import app
from flask import request, jsonify, abort
from sqlalchemy.sql import select, update
from app.database import database
from app.models import Phone
from  app.controllers import auth


# Get list of all phones
@app.route('/phones/', methods=['GET'])
@auth.check_for_token
def getAllphones():
    try:
        return jsonify(get_paginated_list(
		Phone.phones, 
		'/phones/', 
		start=request.args.get('start', 1), 
		limit=request.args.get('limit', 20)
	))
    except Exception as err:
        return jsonify({ 
                'status':'error',
                'message': str(err)
            }) 


# Get user by id
@app.route('/phones/<IdPhone>', methods=['GET'])
@auth.check_for_token
def getPhoneById(IdPhone):
    try:
        result = database.con.execute(Phone.phones.select().where(Phone.phones.c.id==IdPhone)) 
        return jsonify([dict(r) for r in result]) # Print result like json
    except Exception as err:
        return jsonify({ 
                'status':'error',
                'message': str(err)
            }) 


# Insert phone
@app.route('/phones', methods=['POST'])
@auth.check_for_token
def inserPhone():
    try:
        value_ = request.json['value']
        monthyPrice_ = (request.json['monthyPrice'])
        setupPrice_ = (request.json['setupPrice'])
        currency_ = (request.json['currency'])
        if float(setupPrice_)<0.00:
            return jsonify({ 
                'status':'error',
                'message':'Price less than 0.00'
            }) 
        result = database.con.execute(Phone.phones.insert().values(value=value_, monthyPrice=monthyPrice_, setupPrice=setupPrice_, currency=currency_))
        return jsonify({ 
            'status':'success',
            'message':'Phone created with success.'
        })
    except Exception as err:
        return jsonify({ 
                'status':'error',
                'message': str(err)
            }) 

# Update phone
@app.route('/phones/<IdPhone>', methods=['PUT'])
@auth.check_for_token
def updatePhone(IdPhone):
    try:
        value_ = request.json['value']
        monthyPrice_ = (request.json['monthyPrice'])
        setupPrice_ = (request.json['setupPrice'])
        currency_ = (request.json['currency'])
        result = database.con.execute(Phone.phones.update().where(Phone.phones.c.id==IdPhone).values(value=value_,monthyPrice=monthyPrice_, setupPrice=setupPrice_, currency=currency_))
        return jsonify({ 
            'status':'success',
            'message':'Phone updated with success.'
        })
    except Exception as err:
        return jsonify({ 
                'status':'error',
                'message': str(err)
            }) 

# Delete phone
@app.route('/phones/<IdPhone>', methods=['DELETE'])
@auth.check_for_token
def deletePhone(IdPhone):
    try:
        result = database.con.execute(Phone.phones.delete().where(Phone.phones.c.id==IdPhone)) 
        return jsonify({ 
            'status':'success',
            'message':'Phone deleted with success.'
        })
    except Exception as err:
        return jsonify({ 
                'status':'error',
                'message': str(err)
            }) 



# Pagination
def get_paginated_list(klass, url, start, limit):
    # check if page exists
    results = database.con.execute(select([Phone.phones]))
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