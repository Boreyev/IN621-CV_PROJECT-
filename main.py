from cv2 import cv2
from gpiozero import AngularServo

hori_servo = AngularServo(17, min_angle=-90, max_angle=90)  # Initialize horizontal axis servo to GPIO pin 17. Movement is 180 degrees from -90 - 90.
verti_servo = AngularServo(18, min_angle=-90, max_angle=90) # Initialize vertical axis servo to GPIO pin 18. 

font = cv2.FONT_HERSHEY_SIMPLEX #Universal font
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') # Load the cascade

cap = cv2.VideoCapture(0)               # To capture video from webcam.
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 300)  # Set frame width to 300 for universal camera use and performance.
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 150) # Set frame height to 150.
x_array = []
y_array = []

while True:
    ret, img = cap.read()                           # Read the frame
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    # Convert to grayscale
    faces = face_cascade.detectMultiScale(gray, 1.1, minNeighbors=10, 10, minSize=(64,64))    
    

    for (x, y, w, h) in faces:                      
       # Get coordinates from detected face. 
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        xString = str(x)
        yString = str(y)
        # cv2.putText(img, xString + ", " + yString, (20,20), font, 0.7, (204, 204, 204), 1)  
        #Displays current coords (For visual testing).

        hori = x
        verti = y
        print("raw x ", hori)

        if hori > 300: 
            print("exceeded!")
            hori = 300
        elif hori < 0:
            hori = 0
        if verti > 150:
            verti = 150
        elif verti < 0:
            verti = 0

        hori = (x * 0.6 -90)
        verti = (y * 1.2 -90)

        print("horizontal angle", int((x * 0.3) - 90))
        print("vertical angle", int((y * 0.6) - 90))

        x_array.push(hori)
        y_array.push(verti)

        hori_servo.angle = (int(hori))   # Map face coordinates to servo angle. 
        verti_servo.angle = (int(verti))   # Example: X coordinate of 200 is equal to an angle of -60 degrees. 
        


    # cv2.imshow('img', img)
    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
# Release the VideoCapture object
cap.release()