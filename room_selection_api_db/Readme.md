# Docker Images and Containers
build and start containers:
```docker-compose up --build``` 
ensure the containers are running:
```docker-compose up```
if there is a problem with a particular container:
```docker-compose logs {name_of_container}```
if needed, to stop and remove containers:
```docker-compose down```

# MongoDB
to connect to the MongoDB shell:
```docker exec -it mongo mongo```
switch to the appropriate database (here our database is named "db"):
```use db```
query the data:
```db.rooms.find()``` or ```db.rooms.find().pretty()``` depending on output format wanted