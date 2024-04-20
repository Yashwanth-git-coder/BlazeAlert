# BlazeAlert: Intelligent Fire Detection and Emergency Response System

BlazeAlert is an advanced fire incident detection and emergency response system built to swiftly identify fire accidents in any location and notify the relevant authorities for immediate assistance. Leveraging the power of Python, Flask, Google Maps API, front-end technologies, and SMTP for email notifications, BlazeAlert ensures rapid response to fire emergencies, potentially saving lives and minimizing property damage.

## Features:

- **Real-time Fire Detection:** Utilizes advanced algorithms to detect fire incidents in various locations.
- **Location Identification:** Automatically identifies the precise location of the fire incident using Google Maps API.
- **Immediate Notification:** Sends instant alerts to the fire department or emergency responders, providing them with the current address for prompt action.
- **User-Friendly Interface:** Offers a user-friendly front-end interface for easy interaction and monitoring.
- **Email Notifications:** Integrates SMTP for sending email notifications to designated recipients, ensuring reliable communication during emergencies.

## Technologies Used:

- **Python:** The core programming language used for building the backend logic and algorithms.
- **Flask:** A lightweight web framework used for developing the backend server and handling HTTP requests.
- **Google Maps API:** Integrated to accurately determine the geographical location of fire incidents.
- **Front-end Technologies:** HTML, CSS, and JavaScript for developing the user interface.
- **SMTP:** Utilized for sending email notifications to designated contacts.

## Getting Started:

To deploy BlazeAlert and start using its features, follow these steps:

1. **Clone the Repository:**

    https://github.com/Yashwanth-git-coder/BlazeAlert.git

2. **Install Dependencies:**

    pip install -r requirements.txt


3. **Configure API Keys:**
- Obtain API keys for Google Maps API and SMTP for email notifications.
- Update the configuration file (`config.py`) with your API keys.

4. **Run the Application:**

  python main.py


5. **Access the Application:**

Open your web browser and navigate to `http://localhost:5000` to access the BlazeAlert dashboard.

## Contributing:

Contributions to BlazeAlert are welcome! If you'd like to contribute, please fork the repository, make your changes, and submit a pull request. Be sure to follow the [contribution guidelines](CONTRIBUTING.md).

## License:

BlazeAlert is licensed under the [MIT License](LICENSE).
