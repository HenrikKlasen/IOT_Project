import React, { useState, useEffect, useCallback } from 'react';
import logo from './logo.svg';
import './App.css';
import GrafanaGraph from './GrafanaGraph';
import RoomSensors from './RoomSensors';
import '@fortawesome/fontawesome-free/css/all.min.css'; // Import Font Awesome CSS

function App() {
  const [sensorData, setSensorData] = useState([]);
  const [lastUpdate, setLastUpdate] = useState(Date.now());
  const [darkMode, setDarkMode] = useState(() => {
    return localStorage.getItem('darkMode') === 'true';
  });

  useEffect(() => {
    const fetchData = () => {
      fetch('http://localhost:5000/api/sensors')
        .then(response => {
          if (!response.ok) {
            throw new Error('Network response was not ok');
          }
          return response.json();
        })
        .then(data => {
          console.log('Fetched sensor data:', data);
          setSensorData(data.rooms); // Assuming the data structure has rooms array
          setLastUpdate(Date.now());
        })
        .catch(error => {
          console.error('Error fetching sensor data:', error);
        });
    };

    fetchData(); // Fetch data immediately on mount
    const interval = setInterval(fetchData, 60000); // Fetch data every 60 seconds

    return () => clearInterval(interval);
  }, []);

  useEffect(() => {
    document.body.classList.toggle('dark-mode', darkMode);
    localStorage.setItem('darkMode', darkMode);
  }, [darkMode]);

  const isRoomAvailable = useCallback((room) => {
    const now = Date.now();
    return (now - lastUpdate) <= 65000 && sensorData[room] !== null;
  }, [lastUpdate, sensorData]);

  const toggleDarkMode = () => {
    setDarkMode(!darkMode);
  };

  return (
    <div className={`App ${darkMode ? 'dark-mode' : 'light-mode'}`}>
      <header className="App-header">
        <label className="toggle-switch">
          <input type="checkbox" checked={darkMode} onChange={toggleDarkMode} />
          <span className="slider">
          </span>
        </label>
      </header>
      <main className="main-content">
        <GrafanaGraph sensorData={sensorData} gridColor={darkMode ? 'gray' : 'lightgray'} />
        <RoomSensors sensorData={sensorData} isRoomAvailable={isRoomAvailable} />
      </main>
    </div>
  );
}

export default React.memo(App);
