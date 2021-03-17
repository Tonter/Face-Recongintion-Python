import cv2

path = r'D:\Editing\Programming New\Python Projects\Camera Tracking\face.png'

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# imports image
img = cv2.imread(path)

# Converts to gray scale
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(imgGray, 1.1, 5)


for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    
# shows img
cv2.imshow('Face', img)

