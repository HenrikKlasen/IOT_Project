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


// Enable or disable quantity inputs based on checkboxes
function toggleQuantityInput(checkboxId, inputId) {
  const checkbox = document.getElementById(checkboxId);
  const input = document.getElementById(inputId);

  checkbox.addEventListener('change', () => {
    input.disabled = !checkbox.checked;
    if (!checkbox.checked) {
      input.value = ''; // Clear input if disabled
    }
  });
}

// Attach toggle logic to all checkboxes with associated inputs
toggleQuantityInput('computers-checkbox', 'computers-min');
toggleQuantityInput('chairs-checkbox', 'chairs-min');
toggleQuantityInput('tables-checkbox', 'tables-min');

// Extend the gatherPreferences function to only include furniture if selected
function gatherPreferences() {
  const preferences = {
    temperature: parseInt(document.getElementById("temp-slider").value, 10),
    light: parseInt(document.getElementById("light-slider").value, 10),
    humidity: parseInt(document.getElementById("humidity-slider").value, 10),
    co2: parseInt(document.getElementById("co2-slider").value, 10),
    sound: parseInt(document.getElementById("sound-slider").value, 10),
    voc: parseInt(document.getElementById("voc-slider").value, 10),
  };

  // Initialize furniture as an empty object
  const furniture = {};

  // Gather furniture preferences only if selected
  if (document.getElementById('projector-checkbox').checked) {
    furniture.projector = true;
  }
  if (document.getElementById('computers-checkbox').checked) {
    const computersMin = document.getElementById('computers-min').value;
    furniture.computers = computersMin ? parseInt(computersMin, 10) : 0;
  }
  if (document.getElementById('chairs-checkbox').checked) {
    const chairsMin = document.getElementById('chairs-min').value;
    furniture.chairs = chairsMin ? parseInt(chairsMin, 10) : 0;
  }
  if (document.getElementById('tables-checkbox').checked) {
    const tablesMin = document.getElementById('tables-min').value;
    furniture.tables = tablesMin ? parseInt(tablesMin, 10) : 0;
  }

  // Only include furniture in preferences if any item was selected
  if (Object.keys(furniture).length > 0) {
    preferences.furniture = furniture;
  }

  return preferences;
}

// Function to reset all preferences (sliders, checkboxes, JSON)
function resetPreferences() {
  // Reset sliders to their default values (5 for all sliders)
  document.getElementById("temp-slider").value = 5;
  document.getElementById("light-slider").value = 5;
  document.getElementById("humidity-slider").value = 5;
  document.getElementById("co2-slider").value = 5;
  document.getElementById("sound-slider").value = 5;
  document.getElementById("voc-slider").value = 5;

  // Reset the slider value displays
  document.getElementById("temp-value").textContent = "5";
  document.getElementById("light-value").textContent = "5";
  document.getElementById("humidity-value").textContent = "5";
  document.getElementById("co2-value").textContent = "5";
  document.getElementById("sound-value").textContent = "5";
  document.getElementById("voc-value").textContent = "5";

  // Reset checkboxes to unchecked state
  document.getElementById("projector-checkbox").checked = false;
  document.getElementById("computers-checkbox").checked = false;
  document.getElementById("chairs-checkbox").checked = false;
  document.getElementById("tables-checkbox").checked = false;

  // Reset the input fields for furniture (disable them again)
  document.getElementById("computers-min").value = "";
  document.getElementById("chairs-min").value = "";
  document.getElementById("tables-min").value = "";

  // Reset the JSON output area
  const jsonOutput = document.getElementById("preferences-json");
  jsonOutput.textContent = "No preferences applied yet.";
}

// Event listener for the Reset Preferences button
document.getElementById("reset-preferences").addEventListener("click", resetPreferences);

