from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from main import db,app
from config import Config
import uuid
from werkzeug.security import generate_password_hash, check_password_hash

#App setup from config and flask_app

###############################################################################
#Models based on tables

#Auth Table

# @app.route('/auth', methods=['GET'])
# def get_auth():


#User Table
#Get one user

@app.route('/user/<id>', methods=['GET'])
def get_one_user():
    pass

#Get all users
@app.route('/user/get', methods=['GET'])
def get_all_users():
    users = Users.query.all()
    return jsonify(users)


@app.route('/user/create', methods=['POST'])
def create_user():
    data = request.json()

    hashed_pass = generate_password_hash(data['password'],methods='sha256')

    new_user = Users(id=str(uuid.uuid4()),
                        userID = data['userID'],
                        type = data['type'],
                        email= data['email'],
                        password=hashed_pass,
                        phone_number = data['phone_number'],
                        name_first = data['name_first'],
                        name_last = data['name_last'],
                        birthday = data['birthday'],
                        volunteering_Radius_in_MI = data['volunteering_Radius_in_MI'],
                        gender = data['gender'],
                        bio = data['bio'],
                        has_car = data['has_car'],
                        occupation = data['occupation'],
                        considered_Emergency = data['considered_Emergency']
                        )

    db.session.add(new_user)
    db.session.commit()

    return jsonify(new_user)

############################################################################
#Location Tables

#Set location
@app.route('/location/setHome', methods=['POST'])
def set_loc():
    data = request.get_json()
    set_loc = Locations(id = str(uuid.uuid4()),
                userID = data['userID'],
                lat = data['lat'],
                long = data['long'])

    db.session.add(set_loc)
    db.session.commit()

    return jsonify({'message' : 'UserHomeLocation Added!'})



#Get Location
@app.route('/location/getHome/<session_cookie>', methods=['GET'])
def get_loc():
    data = request.get_json()
    get_loc = Locations.query.one()
    return jsonify(get_loc)

############################################################################

#Skills Table


#Create New skill




############################################################################
# if __name__ == '__main__':
#     app.run(debug=True)
#Api requests
