import cv2

cap = cv2.VideoCapture(0)

cap.set(3,640)
cap.set(4,480)

imgBackgroung = cv2.imread('Resources/background.png')


folderModePath = 'Resources/Modes'




while True:
    success, img = cap.read()
    # we have to display web cam over background :

    imgBackgroung[162:162+480,55:55+640] = img

    cv2.imshow("Face Attendance",imgBackgroung)
    cv2.waitKey(1)
