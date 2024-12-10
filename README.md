# IOT Project

### Network
![Image of the network to implement](ProjectNetwork.png)

### Protocol usage

-- DRAFT --

- Commlink A: Serial connection
- Commlink B: MQTT (depending on Arduino Version, MQTT client already on Arduino, transmission via WiFi to Broker, then central logic unit as client subscribed to Commlink B)
- Commlink C/D/E: HTTP

### Workplace criteria

[EU regulations](https://eur-lex.europa.eu/eli/dir/1989/654/)

### Concept plan

![Image of the system architecture](Plan.jpg)

## Required libraries

### Google Calendar API

```bs
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

### Get access to Api Credentials

```bs
pip install python-dotenv
```

### Requirements/Project definitions

[Link to the Google Document](https://docs.google.com/document/d/1DtPbd0KlbSSnF6EsBTUqhglhox-PTNla7lFzBRFeDWA/edit?usp=sharing)
