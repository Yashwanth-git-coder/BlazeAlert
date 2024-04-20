from flask import Flask, render_template, redirect
import geocoder
from geopy.geocoders import OpenCage
from ultralytics import YOLO
import cv2
import cvzone
import mysql.connector

app = Flask(__name__)

# MySQL database connection
mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="questin@7784#",
    database="kukiebase"
)

# Load YOLO model
model = YOLO('fire.pt')

# Reading the classes
classnames = ['fire']


def get_current_location():
    g = geocoder.ip('me')
    return g.latlng


def get_current_address():
    location = get_current_location()
    if location:
        geolocator = OpenCage(api_key='76e21007eef847c4b6da7a5d27b32c65')
        latitude = location[0]
        longitude = location[1]
        try:
            location = geolocator.reverse((latitude, longitude))
            return location.address
        except Exception as e:
            return f"Error occurred: {str(e)}"
    else:
        return "Unable to retrieve current address."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fire_detection')
def fire_detection():
    fire_detected = False  # Flag to track if fire has been detected
    fire_location = None   # Variable to store fire location

    cap = cv2.VideoCapture('fire7.mp4')

    if not cap.isOpened():
        return "Error: Unable to open video stream."

    while True:
        ret, frame = cap.read()
        if not ret:
            return "Error: Unable to read frame from video stream."

        frame = cv2.resize(frame, (640, 480))
        result = model(frame, stream=True)

        # Getting bbox, confidence, and class names information
        for info in result:
            boxes = info.boxes
            for box in boxes:
                confidence = box.conf[0] * 100
                class_idx = int(box.cls[0])
                if confidence > 50 and not fire_detected:
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 5)
                    cvzone.putTextRect(frame, f'{classnames[class_idx]} {confidence:.2f}%', [x1 + 8, y1 + 100],
                                       scale=1.5, thickness=2)
                    print("FIRE DETECTED")
                    fire_detected = True  # Set the flag to True once fire is detected

                    # Get current address if fire is detected
                    fire_location = get_current_location()

                    # Insert the fire location into the database
                    if fire_location:
                        cursor = mydb.cursor()
                        sql = "INSERT INTO locations (latitude, longitude) VALUES (%s, %s)"
                        val = (fire_location[0], fire_location[1])
                        cursor.execute(sql, val)
                        mydb.commit()
                        print("Location inserted into the database")

                    break  # Stop processing once fire is detected

        cv2.imshow('frame', frame)
        if fire_detected:
            break  # Stop the code once fire is detected

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    if fire_detected and fire_location:
        return f"FIRE DETECTED. Location: Latitude - {fire_location[0]}, Longitude - {fire_location[1]}"
    else:
        return "FIRE DETECTED."


@app.route('/fire22')
def fire22():
    # Add code to display fire alert page
    return render_template('fire22.html')


if __name__ == "__main__":
    app.run(debug=True)

