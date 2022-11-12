from cv2 import cv2
from gpiozero import AngularServo
from time import sleep

hori_servo = AngularServo(17, min_angle=-90, max_angle=90)
# verti_servo =AngularServo("STUFF")

font = cv2.FONT_HERSHEY_SIMPLEX #Universal font

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# To capture video from webcam.
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 300)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 150)

while True:
    # Read the frame
    ret, img = cap.read()
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        xString = str(x)
        yString = str(y)
        cv2.putText(img, xString + ", " + yString, (20,20), font, 0.7, (204, 204, 204), 1)        #Displays current coords.

        hori_servo.angle = (x * 0.6 - 90)
        # verti_servo.angle = (y * 1.2 -90)

        print("horizontal angle", x * 0.3 - 90)
        print("vertical angle", y * 1.2 - 90)

    cv2.imshow('img', img)
    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
# Release the VideoCapture object
cap.release()
