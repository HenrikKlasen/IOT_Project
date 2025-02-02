// Constants for API URLs
const API_BASE_URL = 'https://api.example.com';
const PREFERENCES_URL = `${API_BASE_URL}/submit-preferences`;

// Elements Selection
const loginScreen = document.getElementById('loginScreen');
const app = document.getElementById('app');
const loginForm = document.getElementById('loginForm');
const jsonOutput = document.getElementById('jsonOutput');
const apiResponseDiv = document.getElementById('apiResponse');
const loadingIndicator = document.getElementById('loadingIndicator');

// Slider Options
const preferencesConfig = {
    roomSize: {
        options: [
            "<strong>Very Small</strong>: Intimate space (1-2 people).",
            "<strong>Small</strong>: Cozy room for small groups (3-4 people).",
            "<strong>Medium</strong>: Standard room size (5-8 people).",
            "<strong>Large</strong>: Spacious area for larger groups (9-15 people).",
            "<strong>Very Large</strong>: Expansive space for big gatherings (15+ people)."
        ],
        slider: document.getElementById("roomSizeSlider"),
        label: document.getElementById("roomSizeLabel"),
    },
    sound: {
        options: [
            "<strong>Very Quiet</strong>: Below 20 dB - A silent environment.",
            "<strong>Quiet</strong>: 20–40 dB - Minimal background noise.",
            "<strong>Moderate</strong>: 40–60 dB - Balanced noise levels.",
            "<strong>Loud</strong>: 60–80 dB - A lively, noisy environment.",
            "<strong>Very Loud</strong>: Above 80 dB - High noise levels, like a busy street."
        ],
        slider: document.getElementById("soundSlider"),
        label: document.getElementById("soundLabel"),
        weightSlider: document.getElementById("soundWeight"),
        weightLabel: "Importance:",
        flexibilitySlider: document.getElementById("soundFlexibility"),
        flexibilityLabel: document.getElementById("soundFlexibilityLabel"),
        flexibilityOptions: [
            "Flexibility: Very rigid noise preference",
            "Flexibility: Slight noise variations allowed",
            "Flexibility: Moderate noise tolerance",
            "Flexibility: High noise tolerance"
        ]
    },
	voc: {
		options: [
			"<strong>Minimal</strong>: Pristine air quality with no detectable VOCs.",
            "<strong>Low</strong>: Low VOC levels, ensuring fresh air.",
            "<strong>Moderate</strong>: Everyday VOC levels, acceptable quality.",
            "<strong>Enhanced</strong>: Higher VOCs, requiring better ventilation.",
            "<strong>Immersive</strong>: Significant VOC levels, needing mitigation."
		],
		slider: document.getElementById("vocSlider"),
		label: document.getElementById("vocLabel"),
		weightSlider: document.getElementById("vocWeight"),
		weightLabel: "Importance:",
		flexibilitySlider: document.getElementById("vocFlexibility"),
		flexibilityLabel: document.getElementById("vocFlexibilityLabel"),
		flexibilityOptions: [
			"Flexibility: Strictly low VOC levels",
            "Flexibility: Minor VOC variability allowed",
            "Flexibility: Moderate VOC tolerance",
            "Flexibility: High VOC tolerance"
		]
	},

    humidity: {
        options: [
            "<strong>Very Dry</strong>: Below 30% - A dry environment.",
            "<strong>Dry</strong>: 30–40% - Slightly dry but manageable.",
            "<strong>Balanced</strong>: 40–60% - Ideal indoor humidity.",
            "<strong>Humid</strong>: 60–70% - Noticeably humid.",
            "<strong>Very Humid</strong>: Above 70% - High humidity, might feel sticky."
        ],
        slider: document.getElementById("humiditySlider"),
        label: document.getElementById("humidityLabel"),
        weightSlider: document.getElementById("humidityWeight"),
        weightLabel: "Importance:",
        flexibilitySlider: document.getElementById("humidityFlexibility"),
        flexibilityLabel: document.getElementById("humidityFlexibilityLabel"),
        flexibilityOptions: [
            "Flexibility: Minimal Sensory Elements",
            "Flexibility: Some Sensory Elements",
            "Flexibility: Balanced Sensory Experience",
            "Flexibility: Rich Sensory Environment"
        ]
    },
    temperature: {
        options: [
            "<strong>Very Cold</strong>: Below 17°C - A brisk and cool environment.",
            "<strong>Cool</strong>: 17–19°C - Slightly cooler but comfortable.",
            "<strong>Normal</strong>: 19–21°C - Balanced, ideal temperature.",
            "<strong>Warm</strong>: 21–23°C - A cozy and pleasant atmosphere.",
            "<strong>Very Warm</strong>: Above 23°C - Toasty and heated."
        ],
        slider: document.getElementById("temperatureSlider"),
        label: document.getElementById("tempLabel"),
        weightSlider: document.getElementById("temperatureWeight"),
        weightLabel: "Importance:",
        flexibilitySlider: document.getElementById("temperatureFlexibility"),
        flexibilityLabel: document.getElementById("temperatureFlexibilityLabel"),
        flexibilityOptions: [
            "Flexibility: Maintain exact temperature",
            "Flexibility: Slightly deviate from temperature",
            "Flexibility: Moderate temperature tolerance",
            "Flexibility: High temperature tolerance"
        ]
    },
    airQuality: {
        options: [
            "<strong>Not important</strong>: I’m not concerned about air freshness.",
            "<strong>Slightly important</strong>: Some freshness is good, but not essential.",
            "<strong>Important</strong>: I value decent air quality for comfort.",
            "<strong>Very important</strong>: Fresh, clean air is a priority for me.",
            "<strong>Essential</strong>: Exceptional air quality is non-negotiable."
        ],
        slider: document.getElementById("airQualitySlider"),
        label: document.getElementById("airQualityLabel"),
        weightSlider: document.getElementById("airQualityWeight"),
        weightLabel: "Importance:",
        flexibilitySlider: document.getElementById("airQualityFlexibility"),
        flexibilityLabel: document.getElementById("airQualityFlexibilityLabel"),
        flexibilityOptions: [
            "Not important at all",
            "Slightly flexible",
            "Moderately flexible",
            "Very flexible"
        ]
    },
    lighting: {
        options: [
            "<strong>Very dim lighting</strong>: I prefer a very low level of light for a serene, cozy setting.",
            "<strong>Dim lighting</strong>: I like low light levels for a calming effect.",
            "<strong>Soft lighting</strong>: Balanced light for a relaxed and comfortable atmosphere.",
            "<strong>Bright lighting</strong>: A well-lit space helps me focus and feel alert.",
            "<strong>Very bright</strong>: Maximum brightness energizes and keeps me active."
        ],
        slider: document.getElementById("lightingSlider"),
        label: document.getElementById("lightingLabel"),
        weightSlider: document.getElementById("lightingWeight"),
        weightLabel: "Importance:",
        flexibilitySlider: document.getElementById("lightingFlexibility"),
        flexibilityLabel: document.getElementById("lightingFlexibilityLabel"),
        flexibilityOptions: [
            "Flexibility: Very rigid lighting preference",
            "Flexibility: Slight lighting variations allowed",
            "Flexibility: Moderate lighting tolerance",
            "Flexibility: High lighting tolerance"
        ]
    }
};

// Function to update labels based on selected values
function updateLabels() {
    // Update Room Size
    const roomSizeValue = preferencesConfig.roomSize.slider.value;
    preferencesConfig.roomSize.label.innerHTML = preferencesConfig.roomSize.options[roomSizeValue];

    // Update Sound
    const soundValue = preferencesConfig.sound.slider.value;
    preferencesConfig.sound.label.innerHTML = preferencesConfig.sound.options[soundValue];
	
    // Update VOC
    const vocValue = preferencesConfig.voc.slider.value;
    preferencesConfig.voc.label.innerHTML = preferencesConfig.voc.options[vocValue];

    // Update Humidity
    const humidityValue = preferencesConfig.humidity.slider.value;
    preferencesConfig.humidity.label.innerHTML = preferencesConfig.humidity.options[humidityValue];
	
    // Update Temperature
    const temperatureValue = preferencesConfig.temperature.slider.value;
    preferencesConfig.temperature.label.innerHTML = preferencesConfig.temperature.options[temperatureValue];

    // Update Air Quality
    const airQualityValue = preferencesConfig.airQuality.slider.value;
    preferencesConfig.airQuality.label.innerHTML = preferencesConfig.airQuality.options[airQualityValue];

    // Update Lighting
    const lightingValue = preferencesConfig.lighting.slider.value;
    preferencesConfig.lighting.label.innerHTML = preferencesConfig.lighting.options[lightingValue/2];

    // Update Flexibility Labels
    updateFlexibilityLabels();
}

// Function to update Flexibility Labels
function updateFlexibilityLabels() {
    for (const category in preferencesConfig) {
        const config = preferencesConfig[category];
        if (config.flexibilitySlider) { // Check if flexibilitySlider exists
            const flexValue = config.flexibilitySlider.value;
            if (config.flexibilityOptions && config.flexibilityOptions[flexValue]) {
                config.flexibilityLabel.innerHTML = config.flexibilityOptions[flexValue];
            }
        }
    }
}

// Attach event listeners to sliders to update labels dynamically
for (const category in preferencesConfig) {
    const config = preferencesConfig[category];

    if (config.slider) { // Check if main slider exists
        config.slider.addEventListener('input', updateLabels);
    }

    if (config.flexibilitySlider) { // Check if flexibility slider exists
        config.flexibilitySlider.addEventListener('input', updateFlexibilityLabels);
    }
}



// Function to setup sliders
function setupSlider(preference) {
    const { slider, label, options } = preference;

    // Check if slider and label are defined
    if (slider && label) {
        label.innerHTML = options[slider.value]; // Set initial label

        slider.oninput = function() {
            // Check if this.value is within the bounds of options
            if (this.value >= 0 && this.value < options.length) {
                label.innerHTML = options[this.value]; // Update label on input
            }
        };
    }
}

// Assuming you have a function to initialize all sliders
function initializeSliders(preferencesConfig) {
    for (const category in preferencesConfig) {
        setupSlider(preferencesConfig[category]);
    }
}

// Call this function after the DOM is fully loaded
document.addEventListener('DOMContentLoaded', () => {
    initializeSliders(preferencesConfig);
});


// Initialize sliders
Object.values(preferencesConfig).forEach(setupSlider);

// Login Functionality
loginForm.addEventListener('submit', async function(event) {
    event.preventDefault(); // Prevent default form submission

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // Bypass Logic for Testing
    if (username === 'User' && password === 'password') { // Replace with desired credentials // username === 'User' && password === 'password'
        localStorage.setItem('token', 'development-token'); // Fake token for local testing
        loginScreen.style.display = 'none'; // Hide login screen
        app.classList.remove('hidden'); // Show app screen
        return; // Exit the function after bypassing
    }

    // Original API Call (commented out or retained for later use)
    //try {
    //    const response = await fetch(`${API_BASE_URL}/login`, {
    //        method: 'POST',
    //        headers: {
    //            'Content-Type': 'application/json',
    //        },
    //        body: JSON.stringify({ username, password }),
    //    });
//
    //    if (!response.ok) {
    //        throw new Error('Invalid username or password.');
    //    }
//
    //    const data = await response.json();
    //    localStorage.setItem('token', data.token); // Store token in local storage
    //    loginScreen.style.display = 'none'; // Hide login screen
    //    app.classList.remove('hidden'); // Show app screen
    //} catch (error) {
    //    alert(error.message);
    //}
});

// Handle Preferences Form Submission
document.getElementById('preferenceForm').addEventListener('submit', async function(event) {
    event.preventDefault();

    //loadingIndicator.style.display = 'block'; // Show loading indicator

    const userPreferences = gatherPreferences();
    let user_preferences_json = JSON.stringify(userPreferences, null, 2);
    console.log(user_preferences_json);
    // Original API Call (commented out or retained for later use)
    const PREFERENCES_URL = 'http://127.0.0.1:8081/recommend-rooms';
    try {
        const response = await fetch(PREFERENCES_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(userPreferences),
        });
        const responseData = await response.json();
        console.log(responseData);
        displayApiResponse(responseData);
    }
    catch (error) {
        alert(error.message);
    }
   // Call the function to display the simulated API response
   

   // Generate and display JSON output of user preferences
   jsonOutput.value = JSON.stringify(userPreferences, null, 2); // Format JSON nicely

   //loadingIndicator.style.display = 'none'; // Hide loading indicator after processing

});

// Gather preferences from sliders and tiles
function gatherPreferences() {
   const preferences = {
       dateTimeSlotStart : document.getElementById("dateTimeSlotStart").value,
       dateTimeSlotEnd : document.getElementById("dateTimeSlotEnd").value,

       roomSize : { 
          min : getRoomSizeMin(),
          max : getRoomSizeMax()
       },

       weightedCategories : {
          temperature_weight : getTempWeight(),
          co2_weight : getCO2Weight(),
          humidity_weight : getHumidityWeight(),
          voc_weight : getVOCWeight(),
          light_weight : getLightWeight(),
          sound_weight : getSoundWeight()
      },

      optimalValues : {
          temperature_opt : getTemperatureOpt(),
          co2_opt : getCO2Opt(),
          humidity_opt : getHumidityOpt(),
          voc_opt : getVOCOpt(),
          light_opt : getLightOpt(),
          sound_opt : getSoundOpt()
      },

      flexibilityValues : {
          temperature_flexibility : parseInt(document.getElementById("temperatureFlexibility").value), 
          co2_flexibility : parseInt(document.getElementById("airQualityFlexibility").value),
          humidity_flexibility : parseInt(document.getElementById("humidityFlexibility").value),
          voc_flexibility : parseInt(document.getElementById("vocFlexibility").value),
          light_flexibility : parseInt(document.getElementById("lightingFlexibility").value),
          sound_flexibility : parseInt(document.getElementById("soundFlexibility").value)
      },

      facilityRequirements : [
          { name : "Projector", quantity :1 } // Example facility; replace with actual selections if needed.
      ]
   };
    
   return preferences;
}

// Helper functions to calculate ranges and optimal values based on sliders

function getRoomSizeMin() {
   const sizeValue = parseInt(document.getElementById("roomSizeSlider").value);
   const roomRanges = [
       { min : 1 }, // Very Small
       { min : 3 }, // Small
       { min : 5 }, // Medium
       { min : 9 }, // Large
       { min : 15 } // Very Large
   ];
   return roomRanges[sizeValue].min;
}

function getRoomSizeMax() {
   const sizeValue = parseInt(document.getElementById("roomSizeSlider").value);
   const roomRanges = [
       { max : 2 }, // Very Small
       { max : 4 }, // Small
       { max : 8 }, // Medium
       { max : 15 }, // Large
       { max : Infinity } // Very Large (no upper limit)
   ];
   return roomRanges[sizeValue].max;
}

function getTemperatureOpt() {
   const tempValue = parseInt(document.getElementById("temperatureSlider").value);
   const temperatureRanges = [
       { min : 15, max:17 }, // Slider value 0 (<17°C)
       { min:17, max:19 },   // Slider value 1 (17-19°C)
       { min:19, max:21 },   // Slider value 2 (19-21°C)
       { min:21, max:23 },   // Slider value 3 (21-23°C)
       { min:23, max:25 }    // Slider value 4 (>23°C)
   ];
   
   return temperatureRanges[tempValue];
}

function getCO2Opt() {
   const co2Value = parseInt(document.getElementById("airQualitySlider").value);
   const airQualityRanges = [
       2, // Very Small
       4, // Small
       8, // Medium
       15, // Large
       Infinity // Very Large (no upper limit)
   ];
   
   return airQualityRanges[co2Value];
}

function getVOCOpt() {
   const vocValue = parseInt(document.getElementById("vocSlider").value);
   const vocRanges = [
       0, // Slider value 0 (<17°C)
       0.2,   // Slider value 1 (17-19°C)
       0.4,   // Slider value 2 (19-21°C)
       0.6,   // Slider value 3 (21-23°C)
       0.8    // Slider value 4 (>23°C)
   ];
   
   return vocRanges[vocValue];
}

function getHumidityOpt() {
   const humidityValue = parseInt(document.getElementById("humiditySlider").value);
   const humidityRanges = [
       0.0, // Slider value 0 (<17°C)
       .20,   // Slider value 1 (17-19°C)
       .40,   // Slider value 2 (19-21°C)
       .60,   // Slider value 3 (21-23°C)
       .8    // Slider value 4 (>23°C)
   ];
   
   return humidityRanges[humidityValue];
}

function getLightOpt() {
   return parseInt(document.getElementById("lightingSlider").value);
}

function getSoundOpt() {
   const soundValue = parseInt(document.getElementById("soundSlider").value);
   const soundRanges = [
       200, // Slider value 0 (<17°C)
       400,   // Slider value 1 (17-19°C)
       600,   // Slider value 2 (19-21°C)
       800,   // Slider value 3 (21-23°C)
       1000    // Slider value 4 (>23°C)
   ];
   
   return soundRanges[soundValue];
}

function getTempWeight() {
    return parseFloat(document.getElementById("temperatureWeight").value);
}
function getCO2Weight() {
    return parseFloat(document.getElementById("airQualityWeight").value);
}
function getHumidityWeight() {
    return parseFloat(document.getElementById("humidityWeight").value);
}
function getVOCWeight() {
    return parseFloat(document.getElementById("vocWeight").value);
}
function getLightWeight() {
    return parseFloat(document.getElementById("lightingWeight").value);
}
function getSoundWeight() {
    return parseFloat(document.getElementById("soundWeight").value);
}


// Display API Response
function displayApiResponse(data) {
   apiResponseDiv.innerHTML = ''; // Clear previous content
    console.log(data);
   if (!data.length) {
       apiResponseDiv.innerText = 'No rooms available.';
       return;
   }
   for(i in Object.keys(data)) {
         const roomProb = data[i];
         const roomDiv = createRoomInfoDiv(i, roomProb);
         apiResponseDiv.appendChild(roomDiv);
   }
}

// Create HTML structure for room information
function createRoomInfoDiv(roomID, room) {
   const roomDiv = document.createElement('div');
   roomDiv.classList.add('room-info');
   roomDiv.innerHTML = `
     <div class='room-header'>
         <h3><span class='rank-badge'>Match ${room * 100}%</span> Room ID:${roomID}</h3>
     </div>`;
    
   return roomDiv;
}

// Tiles Handling remains the same
// Handle tile click event to toggle selection and quantity input visibility
function handleTileClick(event) {
    const tileElement = event.target.closest('.tile'); // Get the closest tile element

    if (tileElement && !event.target.classList.contains('quantity-input')) {
        // Toggle the selected state of the tile
        tileElement.classList.toggle('selected');

        // Get the quantity input associated with this tile
        const quantityInput = tileElement.querySelector('.quantity-input');

        // Show or hide the quantity input based on the tile's selected state
        if (tileElement.classList.contains('selected')) {
            quantityInput.style.display = 'block'; // Show input if selected
            quantityInput.value = '1'; // Default quantity when selected
        } else {
            quantityInput.style.display = 'none'; // Hide input if not selected
            quantityInput.value = ''; // Clear value when deselected
        }
    }
}

document.querySelectorAll('.tile').forEach(tile => {
    tile.addEventListener('click', handleTileClick);
});

// Logout Functionality
document.getElementById('logoutBtn').addEventListener('click', () => {
   localStorage.removeItem('token');
   app.classList.add('hidden');
   loginScreen.style.display = '';
});

// Reset Form Functionality
document.querySelector('[type=reset]').addEventListener('click', () => {
   jsonOutput.value = ''; // Clear JSON output on reset
});

// Handle Dark Mode Toggle
const darkModeToggle = document.getElementById('darkModeToggle');
darkModeToggle.addEventListener('click', () => {
  document.body.classList.toggle('dark-mode');
});

// Toggle between Preferences and Documentation sections
const preferencesBtn = document.getElementById('preferencesBtn');
const documentationBtn = document.getElementById('documentationBtn');
const preferencesSection = document.getElementById('preferencesSection');
const documentationSection = document.getElementById('documentationSection');

// Initially, show the preferences section and hide documentation
preferencesSection.classList.remove('hidden');
documentationSection.classList.add('hidden');

// Event listeners for the buttons
preferencesBtn.addEventListener('click', () => {
  preferencesSection.classList.remove('hidden');
  documentationSection.classList.add('hidden');
});

documentationBtn.addEventListener('click', () => {
  documentationSection.classList.remove('hidden');
  preferencesSection.classList.add('hidden');
});

function validateDateTime() {
    const startInput = document.getElementById("dateTimeSlotStart");
    const endInput = document.getElementById("dateTimeSlotEnd");
    const errorMessage = document.getElementById("dateTimeError");
    
    const startDateTime = new Date(startInput.value);
    const endDateTime = new Date(endInput.value);
    const currentDateTime = new Date();

    // Clear previous error messages
    errorMessage.textContent = "";

    // Check if start time is in the past
    if (startDateTime < currentDateTime) {
        errorMessage.textContent = "Start date and time cannot be in the past.";
		startInput.value = '';
        return false;
    }

    // Check if end time is after start time
    if (endDateTime <= startDateTime) {
        errorMessage.textContent = "End date and time must be after start time.";
		endInput.value = '';
        return false;
    }
	
    // Check if start time is in the past
    if (endDateTime < currentDateTime) {
        errorMessage.textContent = "End date and time cannot be in the past.";
		endInput.value = '';
        return false;
    }
    return true;
}