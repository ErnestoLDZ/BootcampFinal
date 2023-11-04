import os
from flask import Flask
from flask_restful import Api
#from flask_sqlalchemy import SQLAlchemy
#from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
 
 
from config import app_config
 
app = Flask(__name__)
api = Api(app)
 
#ma = SQLAlchemyAutoSchema()
 
config_name = os.getenv('FLASK_ENV')
app.config.from_object(app_config[config_name])
#db = SQLAlchemy(app)
 
from proyecto_final.rutas import manager_ruta
from proyecto_final.controlador import manager