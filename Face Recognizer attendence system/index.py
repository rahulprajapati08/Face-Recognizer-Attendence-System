import cv2
import face_recognition
import os
import numpy as np
from datetime import datetime

path = 'Known Images'
images = []
classNames = []
myList = os.listdir(path)

for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])


def findEncodings(images):
    encodelist = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(img)
        if len(face_locations) > 0:
            encode = face_recognition.face_encodings(img)[0]
            encodelist.append(encode)
        else:
            print("No faces found in image.")
    return encodelist

encodeListKnown = findEncodings(images)
print("Encodings Complete")

def markattendence(name):
    file_path = 'Attendence.csv'
    
    # Check if the file exists, and create it with headers if not
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            f.write('Name,Time\n')
    
    # Now append the attendance record
    with open(file_path, 'r+') as f:
        myDataList = f.readlines()
        nameList = [line.split(',')[0] for line in myDataList]
        
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtString}')


cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesCurrFrame = face_recognition.face_locations(imgS)
    encodeCurrFrame = face_recognition.face_encodings(imgS, facesCurrFrame)

    for encodeface, faceloc in zip(encodeCurrFrame, facesCurrFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeface)
        facedis = face_recognition.face_distance(encodeListKnown, encodeface)
        matchIndex = np.argmin(facedis)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            y1, x2, y2, x1 = faceloc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            markattendence(name)

    cv2.imshow('WebCam', img)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close windows
cap.release()
cv2.destroyAllWindows()


