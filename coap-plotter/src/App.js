import React, { useState, useEffect } from 'react';
import io from 'socket.io-client';
import Chart from 'react-apexcharts';

const socket = io('http://localhost:4000');

function App() {
  const [timestamps, setTimestamps] = useState([]);
  const [roomTP, setRoomTP] = useState([]);
  const [roomLuminosity, setRoomLuminosity] = useState([]);
  const [roomNoise, setRoomNoise] = useState([]);

  useEffect(() => {
    socket.on('connect', () => {
      console.log('Connected to WebSocket server');
    });

    socket.on('data', (newData) => {
      console.log('Received data:', newData);
      setTimestamps((prev) => [...prev, newData.timestamp]);
      setRoomTP((prev) => [...prev, newData.roomTP]);
      setRoomLuminosity((prev) => [...prev, newData.roomLuminosity]);
      setRoomNoise((prev) => [...prev, newData.roomNoise]);
    });

    socket.on('disconnect', () => {
      console.log('Disconnected from WebSocket server');
    });

    return () => {
      socket.off('data');
      socket.off('connect');
      socket.off('disconnect');
    };
  }, []);

  const roomTPData = {
    series: [{
      name: 'Room Temperature',
      data: roomTP
    }],
    options: {
      chart: {
        type: 'line',
        height: 350,
        animations: {
          enabled: true,
          easing: 'linear',
          dynamicAnimation: {
            speed: 1000
          }
        }
      },
      xaxis: {
        categories: timestamps,
        type: 'datetime',
        labels: {
          format: 'HH:mm:ss'
        }
      },
      yaxis: {
        title: {
          text: 'Temperature (Celsius)'
        }
      }
    }
  };

  const roomLuminosityData = {
    series: [{
      name: 'Room Luminosity',
      data: roomLuminosity
    }],
    options: {
      chart: {
        type: 'line',
        height: 350,
        animations: {
          enabled: true,
          easing: 'linear',
          dynamicAnimation: {
            speed: 1000
          }
        }
      },
      xaxis: {
        categories: timestamps,
        type: 'datetime',
        labels: {
          format: 'HH:mm:ss'
        }
      },
      yaxis: {
        title: {
          text: 'Luminosity (Lux)'
        }
      }
    }
  };

  const roomNoiseData = {
    series: [{
      name: 'Room Noise',
      data: roomNoise
    }],
    options: {
      chart: {
        type: 'line',
        height: 350,
        animations: {
          enabled: true,
          easing: 'linear',
          dynamicAnimation: {
            speed: 1000
          }
        }
      },
      xaxis: {
        categories: timestamps,
        type: 'datetime',
        labels: {
          format: 'HH:mm:ss'
        }
      },
      yaxis: {
        title: {
          text: 'Noise (dB)'
        }
      }
    }
  };

  return (
    <div className="App">
      <h1>Real-Time CoAP Data Plot</h1>
      <div>
        <h2>Room Temperature</h2>
        <Chart options={roomTPData.options} series={roomTPData.series} type="line" height={350} />
      </div>
      <div>
        <h2>Room Luminosity</h2>
        <Chart options={roomLuminosityData.options} series={roomLuminosityData.series} type="line" height={350} />
      </div>
      <div>
        <h2>Room Noise</h2>
        <Chart options={roomNoiseData.options} series={roomNoiseData.series} type="line" height={350} />
      </div>
    </div>
  );
}

export default App;