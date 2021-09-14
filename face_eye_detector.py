import cv2

face_cascade = cv2.CascadeClassifier(r"haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(r"haarcascade_eye_tree_eyeglasses.xml")
cap = cv2.VideoCapture(0) #To capture video from webcam. 

while True:
   
    _, img = cap.read()  #Read the frame

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #Convert to grayscale

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)  #Detect the faces

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)  #Draw the rectangle around each face

    eyes = eye_cascade.detectMultiScale(gray, 1.1, 4)

    for (x1, y1, w1, h1) in eyes:
        cv2.rectangle(img, (x1, y1),(x1+w1, y1+h1), (0,255,0), 2)

    cv2.imshow('img', img) #Display's the cam

    k = cv2.waitKey(30) & 0xff #Stop if escape key is pressed
    if k==27:
        break
        
cap.release() #Release the VideoCapture object