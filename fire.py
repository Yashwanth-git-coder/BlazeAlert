import geocoder
from geopy.geocoders import OpenCage
from ultralytics import YOLO
import cv2
import cvzone
import math

# Load YOLO model
model = YOLO('fire.pt')

# Reading the classes
classnames = ['fire']


# Function to get current location
def get_current_location():
    g = geocoder.ip('me')
    print(g.latlng)
    return g.latlng


# Function to get current address
def get_current_address():
    location = get_current_location()
    if location:
        geolocator = OpenCage(api_key='76e21007eef847c4b6da7a5d27b32c65')  # Replace 'YOUR_API_KEY' with your actual API key
        latitude = location[0]
        longitude = location[1]
        try:
            location = geolocator.reverse((latitude, longitude))
            return location.address
        except Exception as e:
            return f"Error occurred: {str(e)}"
    else:
        return "Unable to retrieve current address."


# Running real-time from webcam
cap = cv2.VideoCapture('fire7.mp4')

if not cap.isOpened():
    print("Error: Unable to open video stream.")
    exit()

fire_detected = False  # Flag to track if fire has been detected

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Unable to read frame from video stream.")
        break

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
                address = get_current_address()
                print("Current Address:", address)

                break  # Stop processing once fire is detected

    cv2.imshow('frame', frame)
    if fire_detected:
        break  # Stop the code once fire is detected

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
