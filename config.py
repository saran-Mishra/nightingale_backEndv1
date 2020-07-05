import os

# utilize os lib
# creating file variable
# __file__ in this case = C:...//backEnd/app.db
#Will create SQlite DB

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # Config DB
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'p2pV1.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
