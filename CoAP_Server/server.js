const coap = require('coap');
const express = require('express');
const http = require('http');
const socketIo = require('socket.io');
const cors = require('cors');

const app = express();
const server = http.createServer(app);
const io = socketIo(server, {
  cors: {
    origin: '*',
    methods: ['GET', 'POST']
  }
});

// Enable CORS
app.use(cors());

// CoAP client setup to observe /Room1
const req = coap.request({
  observe: true,
  hostname: 'localhost', // Replace with your CoAP server's IP address
  port: 5683,
  pathname: '/Room1',
  method: 'GET'
});

req.on('response', (res) => {
  res.on('data', (data) => {
    const parsedData = JSON.parse(data.toString());
    const innerData = JSON.parse(parsedData.data);
    const sensorData = JSON.parse(innerData.data);

    const timestamp = sensorData.timestamp;
    const roomTP = parseFloat(sensorData.sensors.roomTP);
    const roomLuminosity = sensorData.sensors.roomLuminosity;
    const roomNoise = parseFloat(sensorData.sensors.roomNoise);

    console.log('Received data:', { timestamp, roomTP, roomLuminosity, roomNoise });

    // Emit data to all connected WebSocket clients
    io.emit('data', { timestamp, roomTP, roomLuminosity, roomNoise });
  });
});

req.end();

// WebSocket server setup
io.on('connection', (socket) => {
  console.log('New client connected');
  socket.on('disconnect', () => {
    console.log('Client disconnected');
  });
});

server.listen(4000, () => {
  console.log('HTTP server listening on port 4000');
});