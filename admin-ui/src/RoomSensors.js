import React from 'react';

const RoomSensors = ({ sensorData, isRoomAvailable }) => {
  const getStatus = (sensorValues, sensorName) => {
    let consecutiveMisses = 0;
    let missedOnce = false;
    for (let i = 0; i <= sensorValues.length - 1; i++){
      const sensor = sensorValues[i];
      if (sensor[sensorName] == null || sensor[sensorName] === 'none' || sensor[sensorName] === 0) {
        consecutiveMisses++;
        if (consecutiveMisses >= 3) {
          return { status: 'red', misses: consecutiveMisses };
        }
      } else {
        consecutiveMisses = 0;
      }
    }
    
    if (consecutiveMisses > 0) {
      missedOnce = true;
    }

    return { status: missedOnce ? 'yellow' : 'green', misses: consecutiveMisses };
  };

  return (
    <div className="room-sensors">
      {sensorData
        .sort((a, b) => String(a.name).localeCompare(String(b.name))) // Sort by room name
        .map((room, index) => (
          <div key={index} className={`room ${isRoomAvailable(index) ? 'available' : 'unavailable'}`}>
            <h3>Room {room.name}</h3>
            <ul>
              {Object.keys(room.sensors_values[0]).filter(sensorName => sensorName !== 'timestamp').map((sensorName, sensorIndex) => {
                const lastReading = room.sensors_values[room.sensors_values.length - 1][sensorName];
                const { status, misses } = getStatus(room.sensors_values, sensorName);
                return (
                  <li key={sensorIndex} className={`sensor-status ${status}`}>
                    {sensorName}: {status} - Last reading: {lastReading ? lastReading.toFixed(2) : 'N/A'} - Misses: {misses}
                  </li>
                );
              })}
            </ul>
          </div>
        ))}
    </div>
  );
};

export default RoomSensors;
