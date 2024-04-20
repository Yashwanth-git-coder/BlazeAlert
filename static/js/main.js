const button = document.getElementById('getCurrentLocation');
const latitudeDisplay = document.getElementById('latitude');
const longitudeDisplay = document.getElementById('longitude');

function gotLocation(position) {
    console.log(position);
    const latitude = position.coords.latitude;
    const longitude = position.coords.longitude;
    latitudeDisplay.textContent = Latitude: ${latitude};
    longitudeDisplay.textContent = Longitude: ${longitude};
}

function failedToFetch() {
    console.log("Failed to fetch the current location");
}

button.addEventListener("click", async () => {
    navigator.geolocation.getCurrentPosition(gotLocation, failedToFetch)
});