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

  const generateGraphData = (sensorType) => {
    const labels = [];
    const datasets = [];

    sensorData.forEach((room, index) => {
      const data = [];
      room.sensors_values.forEach(sensor => {
        if (labels.length < room.sensors_values.length) {
          labels.push(new Date(sensor.timestamp).toLocaleTimeString());
        }
        data.push(sensor[sensorType]);
      });

      datasets.push({
        label: `Room ${room.name} - ${sensorType}`,
        data,
        fill: false,
        backgroundColor: roomColors[index],
        borderColor: roomColors[index],
      });
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
