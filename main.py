from cv2 import cv2
from gpiozero import AngularServo

hori_servo = AngularServo(17, min_angle=-90, max_angle=90)  # Initialize horizontal axis servo to GPIO pin 17. Movement is 180 degrees from -90 - 90.
verti_servo = AngularServo(18, min_angle=-90, max_angle=90) # Initialize vertical axis servo to GPIO pin 18. 

font = cv2.FONT_HERSHEY_SIMPLEX #Universal font
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') # Load the cascade

cap = cv2.VideoCapture(0)               # To capture video from webcam.
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 300)  # Set frame width to 300 for universal camera use and performance.
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 150) # Set frame height to 150.

while True:
    ret, img = cap.read()                           # Read the frame
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    # Convert to grayscale
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)    

    for (x, y, w, h) in faces:                      # Get coordinates from detected face. 
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        xString = str(x)
        yString = str(y)
        cv2.putText(img, xString + ", " + yString, (20,20), font, 0.7, (204, 204, 204), 1)  #Displays current coords (For visual testing).



        if hori_servo > 300: 
            hori_servo = 300
        elif hori_servo < 0:
            hori_servo = 0
        if verti_servo > 150:
            verti_servo = 150
        elif verti_servo < 0:
            verti_servo = 0

        hori_servo.angle = (x * 0.6 - 90)   # Map face coordinates to servo angle. 
        verti_servo.angle = (y * 1.2 -90)   # Example: X coordinate of 200 is equal to an angle of -60 degrees. 
        
        print("horizontal angle", x * 0.3 - 90)
        print("vertical angle", y * 1.2 - 90)

    cv2.imshow('img', img)
    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
# Release the VideoCapture object
cap.release()
