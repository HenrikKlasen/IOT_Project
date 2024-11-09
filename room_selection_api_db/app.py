from flask import Flask
from flask_pymongo import PyMongo
#from flasgger import Swagger
from setup_db import setupDB

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://mongo:27017/db"
#app.config['SWAGGER'] = { 'title': 'Room Selection API', 'uiversion': 3}
#swagger = Swagger(app)
mongo = PyMongo(app)

#call the setupDB function to initialize the database and collections, and import the data into the database
setupDB(mongo)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


