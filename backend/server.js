const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');

const app = express();
const port = 5000;

app.use(cors());

mongoose.connect('mongodb://localhost:27017/db', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
})
.then(() => console.log('MongoDB connected'))
.catch(err => console.error('MongoDB connection error:', err));

const sensorSchema = new mongoose.Schema({}, { strict: false });
const Sensor = mongoose.model('Sensor', sensorSchema, 'sensors_collection');

app.get('/api/sensors', async (req, res) => {
  console.log('Received request for sensor data');
  try {
    const sensor = await Sensor.findOne({ _id: new mongoose.Types.ObjectId('67682bfaee5c63733df5b3fb') });
    if (!sensor) {
      console.log('No sensor data found');
      return res.status(404).json({ error: 'No sensor data found' });
    }
    console.log('Sending sensor data:', sensor);
    res.json(sensor);
  } catch (error) {
    console.error('Error fetching sensor data:', error);
    res.status(500).json({ error: 'Failed to fetch sensor data', details: error.message });
  }
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
