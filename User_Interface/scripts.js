// scripts.js

// Function to switch between tabs
function switchTab(event, tabId) {
  const allSections = document.querySelectorAll('.tab-content');
  const allButtons = document.querySelectorAll('.tab-buttons button');

  // Hide all sections and remove 'active' class from buttons
  allSections.forEach(section => section.classList.add('hidden'));
  allButtons.forEach(button => button.classList.remove('active'));

  // Show the clicked tab's section and mark the button as 'active'
  document.getElementById(tabId).classList.remove('hidden');
  event.target.classList.add('active');
}

// Attach event listeners to the tab buttons
document.getElementById('preferences-tab-btn').addEventListener('click', (event) => {
  switchTab(event, 'preferences-section');
});

document.getElementById('documentation-tab-btn').addEventListener('click', (event) => {
  switchTab(event, 'documentation-section');
});

// Function to update slider labels dynamically
function updateSliderValue(sliderId, valueId) {
  const slider = document.getElementById(sliderId);
  const valueDisplay = document.getElementById(valueId);

  slider.addEventListener('input', () => {
    valueDisplay.textContent = slider.value;
  });
}

// Attach listeners to all sliders
updateSliderValue("temp-slider", "temp-value");
updateSliderValue("light-slider", "light-value");
updateSliderValue("humidity-slider", "humidity-value");
updateSliderValue("co2-slider", "co2-value");
updateSliderValue("sound-slider", "sound-value");
updateSliderValue("voc-slider", "voc-value");

// Function to gather preferences into a JSON object
function gatherPreferences() {
  const preferences = {
    temperature: parseInt(document.getElementById("temp-slider").value, 10),
    light: parseInt(document.getElementById("light-slider").value, 10),
    humidity: parseInt(document.getElementById("humidity-slider").value, 10),
    co2: parseInt(document.getElementById("co2-slider").value, 10),
    sound: parseInt(document.getElementById("sound-slider").value, 10),
    voc: parseInt(document.getElementById("voc-slider").value, 10),
  };
  return preferences;
}

// Function to display the JSON object
function displayPreferences(preferences) {
  const jsonOutput = document.getElementById("preferences-json");
  jsonOutput.textContent = JSON.stringify(preferences, null, 2); // Pretty-print JSON
}

// Function to download the JSON object as a file
function downloadPreferences(preferences) {
  const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(preferences, null, 2));
  const downloadAnchor = document.createElement("a");
  downloadAnchor.setAttribute("href", dataStr);
  downloadAnchor.setAttribute("download", "preferences.json");
  document.body.appendChild(downloadAnchor);
  downloadAnchor.click();
  document.body.removeChild(downloadAnchor);
}

// Event listener for the Apply Preferences button
document.getElementById("apply-preferences").addEventListener("click", () => {
  const preferences = gatherPreferences();
  displayPreferences(preferences);
});

// Event listener for the Download JSON button
document.getElementById("download-json").addEventListener("click", () => {
  const preferences = gatherPreferences();
  downloadPreferences(preferences);
});
