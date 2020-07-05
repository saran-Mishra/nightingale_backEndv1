from main import db
import csv
import sqlite3

con = sqlite3.connect("C:\\Users\\Saran\\Desktop\\p2pResearch\\backEnd\\nightingale_flask-sqlite-app_v1\\p2pV1.db")
cur = con.cursor()

# Example Auth table

with open('C:\\Users\\Saran\\Desktop\\p2pResearch\\backEnd\\nightingale_flask-sqlite-app_v1\\dummy\\auth.csv') as auth:
    authentication_upload = csv.DictReader(auth)
    to_db_auth = [(i['id'], i['date_created'], i['token']) for i in authentication_upload]

cur.executemany("INSERT INTO Auth (id,date_created,token) VALUES (?,?,?);", to_db_auth)

con.commit()

#Example User Table

with open('C:\\Users\\Saran\\Desktop\\p2pResearch\\backEnd\\dummy\\users.csv') as fin:

    dr = csv.DictReader(fin)
    to_db_users = [(i['user_ID'],i['type'],i['email'],i['password'],i['phone_number'],i['name_first '],i['name_last'], i['birthday'],i['volunteering_Radius_in_MI'],
                    i['gender'],i['bio'],i['has_car'],i['occupation'],i['considered_Emergency']) for i in dr]

cur.executemany("INSERT OR IGNORE INTO Users (userID,type,email,password, phone_number,name_first,name_last, birthday, volunteering_Radius_in_MI,gender,bio, has_car,occupation,considered_Emergency) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?);", to_db_users)

con.commit()

#Example Locations Tables

with open('C:\\Users\\Saran\\Desktop\\p2pResearch\\backEnd\\nightingale_flask-sqlite-app_v1\\dummy\\locations.csv') as l:

    lc = csv.DictReader(l)
    to_db_loc = [(i['user_ID'],i['lat'], i['long'],i['date']) for l in lc]

cur.executemany("INSERT OR IGNORE INTO Locations (userID,lat,long,date) VALUES(?,?,?,?);", to_db_loc)

con.commit()

#Examples Needs Tables
with open('C:\\Users\\Saran\\Desktop\\p2pResearch\\backEnd\\nightingale_flask-sqlite-app_v1\\dummy\\myneeds.csv') as needs:

    myneeds = csv.DictReader(needs)
    to_db_needs = [(i['service_type'],i['need_level'],i['user']) for needs in myneeds]

cur.executemany("INSERT OR IGNORE INTO MyNeeds (service_type,need_level,userID) VALUES(?,?,?);", to_db_needs)

con.commit()

#Examples Skills Table

with open('C:\\Users\\Saran\\Desktop\\p2pResearch\\backEnd\\nightingale_flask-sqlite-app_v1\\dummy\\myskills.csv') as skills:

    MySkills = csv.DictReader(skills)
    to_db_skills = [(i['service_type'],i['skill_level'],i['user']) for skills in MySkills]

cur.executemany("INSERT OR IGNORE INTO MyNeeds (service_type,skill_level,userID) VALUES(?,?,?);", to_db_skills)
con.commit()



con.close()
