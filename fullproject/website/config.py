import os

DB_NAME= "database.db"
UPLOAD_FOLDER = os.path.join("/Users/charlesguthmann/Downloads/techwithtim/fullproject/website/static/uploads")



class Config():
    SECRET_KEY = "charlie"
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{DB_NAME}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = UPLOAD_FOLDER