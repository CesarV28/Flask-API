from flask import Flask
from routes.contacts import contacts
from decouple import config
from flask_cors import CORS

app = Flask(__name__)

# Cors
cors_origin = config('CORS_ORIGIN')
CORS(app, resources={"*": {"origins": cors_origin}})

# Blueprints
app.register_blueprint(contacts, url_prefix='/api/contacts')

# DB
user = config('MYSQL_USER')
password = config('MYSQL_PASSWORD')
host = config('MYSQL_HOST')
database = config('MYSQL_DATABASE')

app.config['SQLALCHEMY_DATABASE_URI']=f'mysql://{user}:{password}@{host}/{database}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False