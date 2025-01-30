from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS
import os
#from flasgger import Swagger
from setup_external_db import setupExternalDB
from setup_central_db import setupCentralDB
#from google_calendar.setup_google_calendar import setupCalendar

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://mongo:27017/db"
#app.config['SWAGGER'] = { 'title': 'Room Selection API', 'uiversion': 3}
#swagger = Swagger(app)
mongo = PyMongo(app)

#call the setupExternalDB and setupCentralDB functions to initialize the databases and collections, and import the data into the databases
setupExternalDB(mongo, os.getcwd()+"/room_selection_api_db/Project_sensor_data/room_facilities_data")
setupCentralDB(mongo, os.getcwd()+"/room_selection_api_db/Project_sensor_data/sensors_data")


#setupCalendar()

if __name__ == '__main__':
    CORS(app.app)
    app.run(debug=True, host='0.0.0.0')


