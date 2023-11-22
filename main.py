import cv2
import os
cap = cv2.VideoCapture(0)

cap.set(3,640)
cap.set(4,480)

imgBackgroung = cv2.imread('Resources/background.png')


folderModePath = 'Resources/Modes'
modePathList = os.listdir(folderModePath)
imgModeList = []
for path in folderModePath:
    imgModeList.append(cv2.imread(os.path.join(folderModePath,path)))

print(len(imgModeList))





while True:
    success, img = cap.read()
    # we have to display web cam over background :

    imgBackgroung[162:162+480,55:55+640] = img

    cv2.imshow("Face Attendance",imgBackgroung)
    cv2.waitKey(1)
