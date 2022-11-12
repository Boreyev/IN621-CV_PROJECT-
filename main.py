from cv2 import cv2
from gpiozero import Servo
from time import sleep

servo = Servo(17)

def turnRight():    #Turn right when deviated from center. 
    servo.max()
    print("Turn Right")

def turnLeft():     #Turn right when deviated from center. 
    print("Turn Left")

def pivotUp():      #Turn up when deviated from center. 
    print("Pivot Up")

def pivotDown():    #Turn down when deviated from center. 
    print("Pivot Down")


font = cv2.FONT_HERSHEY_SIMPLEX #Universal font

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# To capture video from webcam.
cap = cv2.VideoCapture(0)

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

        if x > 300:
            turnRight()
        elif x < 300:
            turnLeft()
        if y > 125:
            pivotDown()
        elif y < 125:
            pivotUp()

    cv2.imshow('img', img)
    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
# Release the VideoCapture object
cap.release()
