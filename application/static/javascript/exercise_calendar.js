const calendarGrid = document.getElementById('calendarGrid');
const addEventBtn = document.getElementById('addEventBtn');
const eventModal = document.getElementById('eventModal');
const saveEventBtn = document.getElementById('saveEventBtn');
const eventNameInput = document.getElementById('eventName');
const eventDateInput = document.getElementById('eventDate');
const closeBtn = document.querySelector('.close');

addEventBtn.addEventListener('click', () => {
    eventModal.style.display = 'block';
});

closeBtn.addEventListener('click', () => {
    eventModal.style.display = 'none';
});

saveEventBtn.addEventListener('click', () => {
    const eventName = eventNameInput.value;
    const eventDate = eventDateInput.value;

    if (eventName && eventDate) {
        const event = document.createElement('div');
        event.className = 'day';
        event.textContent = eventName;
        event.title = eventDate;
        calendarGrid.appendChild(event);
        eventNameInput.value = '';
        eventDateInput.value = '';
        eventModal.style.display = 'none';
    } else {
        alert('Please fill in all fields.');
    }
});