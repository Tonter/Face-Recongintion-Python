# open cv
import cv2

# Face recognition
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
profile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_profileface.xml')

# Open the device at the ID 0 
cap = cv2.VideoCapture(0)

# Check whether user selected camera is opened successfully.
if cap.isOpened():
    print(">Found capture device")
else:
    print(">Couldnt find capture device")

size = 40

# To set the resolution 
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1080)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

print(">Press 'q' to quit window")

# Capturing frames and showing them
while(True):
    # Captures a frame
    ret, frame = cap.read()

    # Converts frame to gray
    frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Gets face cordinates
    faces = face_cascade.detectMultiScale(frameGray, 1.2, 5)
    # Gets profile cordinates
    profiles = profile_cascade.detectMultiScale(frameGray, 1.1, 5)
    
    for (x, y, w, h) in faces:
        # Draws a rectangel with the face cords
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        topLeft = (x, y-5)
        # Adds a text at the top left
        cv2.putText(frame, 'frontal face', topLeft, cv2.FONT_HERSHEY_SIMPLEX , 1, (255, 0, 0), 2) 
    
    for (x, y, w, h) in profiles:
        # Draws a rectangel with the face cords
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        topLeft = (x, y-5)
        # Adds a text at the top left
        cv2.putText(frame, 'profile', topLeft, cv2.FONT_HERSHEY_SIMPLEX , 1, (0, 0, 255), 2)

        
    # Display the resulting frame
    cv2.imshow("Camera Feed", frame)

    # Waits for a user input to quit the application
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyWindow('Camera Feed')
        print(">Capture Closed")
        break
