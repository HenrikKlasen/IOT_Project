from flask import Flask
from flask_pymongo import PyMongo
#from flasgger import Swagger
from room_selection_api_db.setup_external_db import setupExternalDB
from room_selection_api_db.setup_central_db import setupCentralDB
from google_calendar.setup_google_calendar import setupCalendar

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://mongo:27017/db"
#app.config['SWAGGER'] = { 'title': 'Room Selection API', 'uiversion': 3}
#swagger = Swagger(app)
mongo = PyMongo(app)

#call the setupExternalDB and setupCentralDB functions to initialize the databases and collections, and import the data into the databases
setupExternalDB(mongo)
setupCentralDB(mongo)

setupCalendar()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


