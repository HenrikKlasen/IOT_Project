# Docker Images and Containers
<!-- build and start containers:
```docker-compose up --build``` 
ensure the containers are running:
```docker-compose up```
if there is a problem with a particular container:
```docker-compose logs {name_of_container}```
if needed, to stop and remove containers:
```docker-compose down``` -->

## Create mongodb container in Docker
- Download docker then go to the path where the project is "C:\...\IOT_Project" and run these command in the terminal:
   - ```docker pull mongodb/mongodb-community-server:latest```
   - ```docker run --name mongodb -p 27017:27017 -d mongodb/mongodb-community-server:latest```
- checks the containers in your docker
   - ```docker container ls```

## Create the db
Run the script: room_selection_api_db.setup_db_test.py

## Navigate the db through the terminal
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