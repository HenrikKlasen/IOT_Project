document.addEventListener('DOMContentLoaded', (event) => {
    const form = document.getElementById('preferenceForm');

    // Fetch room data from the backend API
    fetch('/api/rooms')
        .then(response => response.json())
        .then(data => {
            populateRoomOptions(data);
        })
        .catch(error => {
            console.error('Error fetching room data:', error);
        });

    // Populate room options in the form
    function populateRoomOptions(rooms) {
        const roomSelect = document.createElement('select');
        roomSelect.setAttribute('id', 'roomSelect');
        roomSelect.setAttribute('name', 'room');
        form.insertBefore(roomSelect, form.firstChild);

        rooms.forEach(room => {
            const option = document.createElement('option');
            option.value = room.name;
            option.textContent = room.name;
            roomSelect.appendChild(option);
        });
    }
});
