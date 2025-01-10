import React from 'react';
import { Line } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

const GrafanaGraph = ({ sensorData, gridColor }) => {
  const roomColors = ['rgba(75,192,192,1)', 'rgba(255,99,132,1)', 'rgba(54,162,235,1)'];
  const twelveHoursAgo = Date.now() - 12 * 60 * 60 * 1000;

  const generateGraphData = (sensorType) => {
    const labelsSet = new Set();
    const roomData = sensorData.map(room => {
      return room.sensors_values
        .filter(sensor => new Date(sensor.timestamp).getTime() >= twelveHoursAgo) // Filter out old datapoints
        .map(sensor => {
          labelsSet.add(sensor.timestamp);
          return { timestamp: sensor.timestamp, value: sensor[sensorType] };
        });
    });

    const labels = Array.from(labelsSet).sort((a, b) => new Date(a) - new Date(b)).map(timestamp => new Date(timestamp).toLocaleTimeString());

    const datasets = sensorData.map((room, index) => {
      const data = labels.map(label => {
        const sensor = room.sensors_values.find(sensor => new Date(sensor.timestamp).toLocaleTimeString() === label);
        return sensor ? sensor[sensorType] : null;
      });

      return {
        label: `Room ${room.name} - ${sensorType}`,
        data,
        fill: false,
        backgroundColor: roomColors[index],
        borderColor: roomColors[index],
        showLine: true, // Ensure the data is displayed as lines
        pointRadius: 3, // Show the points
      };
    });

    return {
      labels,
      datasets,
    };
  };

  const options = {
    scales: {
      x: {
        grid: {
          color: gridColor,
        },
        ticks: {
          color: gridColor, // Ensure tick color matches grid color
        },
      },
      y: {
        beginAtZero: true,
        grid: {
          color: gridColor,
        },
        ticks: {
          color: gridColor, // Ensure tick color matches grid color
        },
      },
    },
    maintainAspectRatio: false,
  };

  return (
    <div className="graph-grid">
      {['temperature', 'humidity', 'light_intensity', 'sound_level', 'co2_level', 'PM2.5', 'PM10', 'VOC_level'].map(sensorType => (
        <div key={sensorType}>
          <h3>{sensorType}</h3>
          <Line data={generateGraphData(sensorType)} options={options} />
        </div>
      ))}
    </div>
  );
};

export default GrafanaGraph;
