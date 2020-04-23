from flask import Flask
from flask import request
from flask import jsonify

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# init app
app = Flask(__name__)

# database location
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

# init database
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Setting up a class/model for the database. 
class User(db.Model):
    id = db.Column(db.Integer, primary_key = True) #id is autoincremented 
    name = db.Column(db.String(50))
    address = db.Column(db.String(150))
    phone = db.Column(db.Integer)

    # Constructors/initilizers
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone

# creating a schema for a "user"
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'address', 'phone')

# init schema
# GET operation returns a list of users and has multiple elements thefore UserSchema() needs the paramater many = True.
# updating, adding or deleting a user is only done one at a time therefore there are two version of UserSchema()
user_schema = UserSchema()
users_schema = UserSchema(many=True)

# adding a new user 
@app.route('/user', methods=['POST'])
def add_user():
    name = request.json['name']
    address = request.json['address']
    phone = request.json['phone']

    new_user = User(name, address, phone)

    db.session.add(new_user)
    db.session.commit()

    #only adding one user at a time thefore user_schema is used. 
    return user_schema.jsonify(new_user)

# get all users
@app.route('/user', methods=['GET'])
def get_users():
    all_users = User.query.all()

    results = users_schema.dump(all_users) 
    return jsonify(results)

# returns a list of ID that matches the parameter
@app.route('/user/<name>', methods=['GET'])
def get_user(name):
    user = User.query.filter_by(name=name).all()

    return f'ID: {user}'

# get a single user by ID
@app.route('/<id>', methods=['GET'])
def get_user_by_id(id):
    user = User.query.get(id)

    return user_schema.jsonify(user)

# update a user by ID
@app.route('/<id>', methods=['PUT'])
def update_user(id):
    user = User.query.get(id)

    name = request.json['name']
    address = request.json['address']
    phone = request.json['phone']

    # this does the updating
    user.name = name
    user.address = address
    user.phone = phone

    db.session.commit()

    return user_schema.jsonify(user)

# delete a user by ID
@app.route('/<id>', methods=['DELETE'])
def delete_user_by_id(id):
    user = User.query.get(id)

    db.session.delete(user)
    db.session.commit()

    return user_schema.jsonify(user)

# run the server
if __name__ == '__main__':
    app.run(debug=True)