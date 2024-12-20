# IOT Project

### Network
![Image of the network to implement](ProjectNetwork.png)

### Protocol usage

-- DRAFT --

- Commlink A: Serial connection
- Commlink B: MQTT (depending on Arduino Version, MQTT client already on Arduino, transmission via WiFi to Broker, then central logic unit as client subscribed to Commlink B)
- Commlink C/D/E: HTTP
![Image of the system architecture](Plan.jpg)
### Workplace criteria

[EU regulations](https://eur-lex.europa.eu/eli/dir/1989/654/)

### ![Image of the system architecture](Plan.jpg)

# IOT_Project_Arduino_Controller

# IOT_Project_Database

### Create mongodb container in Docker
- Download docker then go to the path where the project is "C:\...\IOT_Project" and run these command in the terminal:
   - ```docker pull mongodb/mongodb-community-server:latest```
   - ```docker run --name mongodb -p 27017:27017 -d mongodb/mongodb-community-server:latest```
- checks the containers in your docker
   - ```docker container ls```

### Create the db
Run the script: room_selection_api_db.setup_db_test.py

### Navigate the db through the terminal
- access the db through the terminal
   - ```mongosh --port 27017```
- Switch to your database (if it exists)
   - ```show dbs```
   - ```use db```
- List all collections in the database
   - ```show collections```
- Check if collections contain any documents
   - ```db.sensors_collection.findOne()```
- If there is already data, delete the data inside the collection to avoid duplicate data
(the script to automatically delete duplicate will be written later)
   - ```db.sensors_collection.deleteMany({})```
- Check content of the collection
   - ```db.rooms_collection.find()``` or ```db.rooms_collection.find().pretty()``` depending on output format wanted
   - ```db.sensors_collection.find({'name': 'Room_1'}).count()```
   - ```db.sensors_collection.find().count()```
- To quit mongosh
   - ```quit```

## Required libraries:

#### Google Calendar API
```pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib```

#### Get access to Api Credentials
```pip install python-dotenv```
### Requirements/Project definitions
![Link to the Google Document](https://docs.google.com/document/d/1DtPbd0KlbSSnF6EsBTUqhglhox-PTNla7lFzBRFeDWA/edit?usp=sharing)
