from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import requests

#configuring flask application and sqlalchemy
app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

