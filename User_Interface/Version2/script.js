// Toggle between Preferences and Documentation sections
const preferencesBtn = document.getElementById('preferencesBtn');
const documentationBtn = document.getElementById('documentationBtn');
const preferencesSection = document.getElementById('preferencesSection');
const documentationSection = document.getElementById('documentationSection');

// Event listeners for the buttons
preferencesBtn.addEventListener('click', () => {
  preferencesSection.classList.remove('hidden');
  documentationSection.classList.add('hidden');
});

documentationBtn.addEventListener('click', () => {
  documentationSection.classList.remove('hidden');
  preferencesSection.classList.add('hidden');
});

// Handle form submission and display JSON output
const form = document.getElementById('preferenceForm');
const jsonOutput = document.getElementById('jsonOutput');

form.addEventListener('submit', function (e) {
  e.preventDefault(); // Prevent the form from submitting and refreshing the page

  // Get form data as an object
  const formData = new FormData(form);
  const userPreferences = {};

  // Iterate through FormData and create an object with key-value pairs
  formData.forEach((value, key) => {
    userPreferences[key] = value;
  });

  // Convert the preferences object into JSON and display it in the textarea
  jsonOutput.value = JSON.stringify(userPreferences, null, 2);
});

// Handle form reset
const resetButton = document.querySelector('[type="reset"]');
resetButton.addEventListener('click', () => {
  jsonOutput.value = ''; // Clear the JSON output when the form is reset
});
