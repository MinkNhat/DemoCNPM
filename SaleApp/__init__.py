from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote
from flask_login import LoginManager
import cloudinary

app = Flask(__name__)

app.secret_key = "$%$##$$JACSKC%@"
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:%s@localhost/saledb?charset=utf8mb4' % quote('Admin@123')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["PAGE_SIZE"] = 8

login = LoginManager(app=app)
db = SQLAlchemy(app)

cloudinary.config(cloud_name='dbmwgavqz',
                  api_key='747824214758252',
                  api_secret='IjgCUhqhoxQhoiG1dcq-vWJk5wA')
