import React from 'react';

const RoomSensors = ({ sensorData, isRoomAvailable }) => {
  console.log('Rendering RoomSensors with data:', sensorData);

  return (
    <div>
      <h2>Room Sensors</h2>
      {Object.keys(sensorData).map(room => (
        <div key={room}>
          <h3>{room}</h3>
          <p>Status: {isRoomAvailable(room) ? 'Available' : 'Unavailable'}</p>
          <p>Sensors: {JSON.stringify(sensorData[room])}</p>
        </div>
      ))}
    </div>
  );
};

export default RoomSensors;
