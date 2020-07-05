import os
from datetime import datetime
from config import Config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


#Script to create Tables in SQLite DBs

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)


migrate = Migrate(app,db)


#Script to create Tables


####################################################
#No levels --- flat wide DB

class Auth(db.Model):

    __tablename__ = 'Auth'

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)

    userID = db.relationship('Users', backref='userAuth')

    date_created = db.Column(db.DateTime, default = datetime.now)

    token = db.Column(db.String(20), unique=True)

    def __init__(userID,date_created,token):
        self.date_created = date_created
        self.userID = userID
        self.token = token

    def __repr__(self):

        return("Hello, this user_ID is %s." %self.user_ID)

class Users(db.Model):

    __tablename__ = 'Users'

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)

    userID = db.Column(db.Integer, db.ForeignKey('Auth.id'))

    type = db.Column(db.Boolean)
    email = db.Column(db.String(500))
    password = db.Column(db.String(150))
    phone_number = db.Column(db.String(12))
    name_first = db.Column(db.String(150))
    name_last = db.Column(db.String(150))
    birthday = db.Column(db.DateTime)
    volunteering_Radius_in_MI = db.Column(db.Integer)
    gender = db.Column(db.String(12)) #could be boolean
    bio = db.Column(db.String(1000))
    has_car = db.Column(db.Boolean)
    occupation = db.Column(db.String(50))
    considered_Emergency = db.Column(db.Boolean)

    def __init__(userID,email, password, phone_number,name_first,name_last,birthday,volunteering_Radius_in_MI, gender, bio, has_car,occupation,considered_Emergency):
        self.userID = userID
        self.email = email
        self.password = password
        self.phone_number = phone_number
        self.name_first = name_first
        self.name_last = name_last
        self.birthday = birthday
        self.volunteering_Radius_in_MI = volunteering_Radius_in_MI
        self.gender = gender
        self.bio = bio
        self.has_car = has_car
        self.occupation = occupation
        self.considered_Emergency = considered_Emergency

    def json(self):
        return {"'userID': %s" %self.userID, "'email': %s" %self.email}

    def __repr__(self):

        return("Hello, %s." %self.name_first)
#

class Locations(db.Model):

        __tablename__ = 'Locations'

        id = db.Column(db.Integer,primary_key=True,autoincrement=True)

        userID =  db.Column(db.Integer, db.ForeignKey('Users.userID'))

        lat = db.Column(db.Numeric(50))
        long = db.Column(db.Numeric(50))

        date = db.Column(db.DateTime())

        def __init__(user_ID,lat,long,date):
            self.user_ID = user_ID
            self.lat = lat
            self.long = long
            self.date = date

        def __repr__(self):

            return("Hello, %s exists on the table." %self.user_ID)

#
class preferences(db.Model):

        __tablename__ = 'preferences'

        id = db.Column(db.Integer,primary_key=True,autoincrement=True)
        userID =  db.Column(db.Integer, db.ForeignKey('Users.userID'))

        service_type = db.Column(db.String(50))

        age_preference = db.Column(db.Numeric)
        rating_preferences = db.Column(db.Numeric)
        gender_preferences = db.Column(db.String(50))
        skill_level_preferences = db.Column(db.String(50))

        def __init__(user_ID,service_type,age_preference,rating_preferences,gender_preferences,skill_level_preferences):
            self.userID = userID
            self.service_type = service_type
            self.age_preference = age_preference
            self.ratings_preferences = rating_preferences
            self.gender_preferences = gender_preferences
            self.skill_level_preferences = skill_level_preferences



        def __repr__(self):

            return("Hello, %s exists on the table." %self.user_ID)

#
class MySkills(db.Model):

        __tablename__ = 'MySkills'

        id = db.Column(db.Integer,primary_key=True,autoincrement=True)

        userID =  db.Column(db.Integer, db.ForeignKey('Users.userID'))

        service_type = db.Column(db.String(50))
        skill_level = db.Column(db.Numeric)

        def __init__(user_ID,service_type,skill_level):
            self.user_ID = user_ID
            self.service_type = service_type
            self.skill_level = skill_level

        def __repr__(self):

            return("Hello, %s exists on the table with skill %s." %(self.user_ID,self.service_type))


#
class MyNeeds(db.Model):

        __tablename__ = 'MyNeeds'

        id = db.Column(db.Integer,primary_key=True,autoincrement=True)
        service_type = db.Column(db.String(50))
        need_level = db.Column(db.Integer)
        userID =  db.Column(db.Integer, db.ForeignKey('Users.userID'))

        #urgency_level = db.Column(db.Integer)
#
class Reviews(db.Model):
        __tablename__ = 'Reviews'

        id = db.Column(db.Integer,primary_key=True,autoincrement=True)
        date = db.Column(db.DateTime, default = datetime.now)
        service_type = db.Column(db.String(50))
        description = db.Column(db.String(100))
        ratings = db.Column(db.Numeric)
        created_by = db.Column(db.Integer)
        about_user = db.Column(db.String(100))

        posting_id = db.Column(db.Integer, db.ForeignKey('Posting.id'))



        def __init__(date,service_type,description,ratings,created_by,about_user,posting_id):
            self.date = date
            self.service_type = service_type
            self.description = description
            self.ratings = ratings
            self.created_by = created_by
            self.about_user = about_user
            self.posting_id = posting_id

        def __repr__(self):

            return("Hello, %s exists on the table with posting ID %s." %(self.user_ID,self.posting_id))

#
class Posting(db.Model):

        __tablename__ = 'Posting'


        id = db.Column(db.Integer,primary_key= True, autoincrement=True)

        posting_id = db.relationship('Reviews', backref='userReviews') #Fake Column

        receipient =  db.Column(db.Integer, db.ForeignKey('Users.userID'))
        provider =  db.Column(db.Integer, db.ForeignKey('Users.userID'))
        deliverer = db.Column(db.Integer, db.ForeignKey('Users.userID'))

        receipient_fk = db.relationship("Users", backref="user", uselist=False, foreign_keys=[receipient])
        provider_fk = db.relationship("Users", backref="user", uselist=False, foreign_keys=[provider])
        deliverer_fk = db.relationship("Users", backref="user", uselist=False, foreign_keys=[provider])



        type = db.Column(db.String(150))
        service_type = db.Column(db.String(50))
        description = db.Column(db.String(500))
        expiration_date = db.Column(db.DateTime)
        created_date = db.Column(db.DateTime)
        matched_date =  db.Column(db.DateTime)
        completed_date =  db.Column(db.DateTime)
        is_match = db.Column(db.Boolean)
        is_complate = db.Column(db.Boolean)
        radius_in_MI = db.Column(db.Integer)

        def __init__(receipient,provider,deliverer,type,service_type,description,expiration_date,created_date,matched_date,completed_date,is_match,is_complete,radius_in_MI):

            self.receipient = receipient
            self.provider = provider
            self.deliverer = deliverer
            self.type = type
            self.service_type = service_type
            self.description = description
            self.expiration_date = expiration_date
            self.created_date = created_date
            self.matched_date = matched_date
            self.completed_date = completed_date


#
class Messages(db.Model):

        __tablename__ = 'Messages'

        id = db.Column(db.Integer,primary_key= True, autoincrement=True)

        match_id = db.Column(db.Integer, db.ForeignKey('Match.id'))

        sender = db.Column(db.Integer)
        receiver = db.Column(db.Integer)

        sender_fk = db.relationship("Posting", backref="user_sender", uselist=False, foreign_keys=[sender])
        receiver_fk = db.relationship("Posting", backref="use_receiverr", uselist=False, foreign_keys=[receiver])

        message = db.Column(db.String(1000))

        date_sent = db.Column(db.DateTime)
        read_status = db.Column(db.Boolean)

        def __init__(posting_id,sender,message,date_sent,read_status):

            self.posting_id = posting_id
            self.sender = sender
            self.receiver = receiver
            self.message = message
            self.date_sent = date_sent
            self.read_status = read_status


#

class Match(db.Model):

        __tablename__ = "Match"

        id = db.Column(db.Integer,primary_key= True, autoincrement=True)

        poster = db.Column(db.Integer,db.ForeignKey('Users.userID'))
        matched_with = db.Column(db.Integer,db.ForeignKey('Users.userID'))

        poster_fk = db.relationship("Users", backref="user", uselist=False, foreign_keys=[poster])
        matched_with_fk= db.relationship("Users", backref="user", uselist=False, foreign_keys=[matched_with])

        posting_id =db.Column(db.Integer, db.ForeignKey('Posting.id'))
        postingID_fk = db.relationship("Posting", backref="postingID", uselist=False, foreign_keys=[posting_id])

        matched_date = db.Column(db.DateTime)

        matched_with_user_accepts = db.Column(db.Boolean)

        post_accepts = db.Column(db.Boolean)

        score = db.Column(db.Integer)

        def __init__(poster,matched_with,posting_id,matched_date,matched_with_user_accepts,post_accepts,score):

            self.poster = poster
            self.matched_with = matched_with
            self.posting_id = posting_id
            self.matched_date = matched_date
            self.matched_with_user_accepts = matched_with_user_accepts
            self.post_accepts = post_accepts
            self.score = score


# ###################################################

db.create_all()
db.session.commit()


# #Fin
