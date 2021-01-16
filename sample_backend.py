from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
import random
app = Flask(__name__)
CORS(app)

users = {
   'users_list' :
   [
      {
         'id' : 'xyz789',
         'name' : 'Charlie',
         'job': 'Janitor',
      },
      {
         'id' : 'abc123',
         'name': 'Mac',
         'job': 'Bouncer',
      },
      {
         'id' : 'ppp222',
         'name': 'Mac',
         'job': 'Professor',
      },
      {
         'id' : 'yat999',
         'name': 'Dee',
         'job': 'Aspring actress',
      },
      {
         'id' : 'zap555',
         'name': 'Dennis',
         'job': 'Bartender',
      }
   ]
}

def randID(name):
    return name+str(random.randint(0,1000))

@app.route('/')
def hello_world():
    return 'Hello, world!'


@app.route('/users', methods=['GET', 'POST', 'DELETE'])
def get_users():
    if request.method == 'GET':
        search_username = request.args.get('name')
        if search_username:
            subdict = {'users_list': []}
            for user in users['users_list']:
                if user['name'] == search_username:
                    subdict['users_list'].append(user)
            return subdict
        return users
    elif request.method == 'POST':
        userToAdd = request.get_json()
        userToAdd['id'] = randID(userToAdd['name'])
        users['users_list'].append(userToAdd)
        resp = jsonify(success=True, user=userToAdd)
        resp.status_code = 201
        # resp.status_code = 200 #optionally, you can always set a response code.
        # 200 is the default code for a normal response
        return resp
    elif request.method == 'DELETE':
        userToDelete = request.get_json()
        users['users_list'].remove(userToDelete)
        resp = jsonify(success=True)
        return resp


@app.route('/users/<id>')
def get_user(id):
   if id :
      for user in users['users_list']:
        if user['id'] == id:
           return user
      return ({})
   return users


@app.route('/users/<name>/<job>')
def get_user_name(name, job):
   if name and job :
      for user in users['users_list']:
        if user['name'] == name and user['job'] == job:
           return user
      return ({})
   return users