import datetime
from flask_bcrypt import Bcrypt  
from werkzeug.security import generate_password_hash
# from flask.ext.bcrypt import generate_password_hash
from flask_login import UserMixin
# from common import db 
# from flasker import db
import pymysql
# from peewee import *

# DATABASE = SqliteDatabase('social.db')
# Open database connection 連線
db = pymysql.connect( host ="localhost",user ="root",password = "mypassword",database = "assignment" )
# prepare a cursor object using cursor() method 使用建立好的游標的execute方法將資料庫表或記錄建立到資料庫表中
cursor = db.cursor()

class User(UserMixin):

    # Drop table if it already exist using execute() method.
    try:
        cursor.execute("DROP TABLE IF EXISTS user")
        # Create table as per requirement
        sql = """CREATE TABLE `user` (
        `id` int(10) NOT NULL AUTO_INCREMENT,
        `email` char(20) NOT NULL,
        `password` char(20) DEFAULT NULL,
        PRIMARY KEY (`id`)
        ) 
        ENGINE=InnoDB DEFAULT CHARSET=utf8;"""
        cursor.execute(sql)
    except:
        db.rollback()

    # @classmethod
    def create_user(email, password):
        try:
            sql = "INSERT INTO `user` (`email`, `password`) VALUES (%s, %s)"
            cursor.execute(sql, (email, password)) 
            db.commit()
        except IntegrityError:
            raise ValueError("User already exists")

    # @classmethod    
    # def select_user(email):
    #     try:
    #         cursor.execute("SELECT * FROM user WHERE email = %s", (email))
    #         user = cursor.fetchone()
    #         for row in user:
    #             email = row[1]
    #     except:
    #         return None
    # def select_user(email):
    #     cursor = db.cursor(pymysql.cursors.DictCursor)
    #     cursor.execute('SELECT * FROM user WHERE email = %s', (email))
    #     try:
    #         user = cursor.fetchone() # a dict
    #         if user:
    #             email = user[1]
    #             return email
    #     except:
    #         return None
    def select_user(email):
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute('SELECT `email` FROM user WHERE email = %s', (email))
        try:
            email = cursor.fetchone()[0]["email"]
            if email:
                return email
        except:
            return None

def initialize():
    # db.create_tables([User], safe=True) # def create_user
    db.create_user()
    db.close()