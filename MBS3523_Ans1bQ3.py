import cv2
print(cv2.__version__)
cam = cv2.VideoCapture(0)
cam.set(3,640)
cam.set(4,480)
x = 0
dx = 1
y = 0
dy = 1

while True:
    success, img = cam.read()
    cv2.putText(img, "MBS3523 Assignment 1b-Q3 Name: Hui Chak Fan",(110,40), cv2.FONT_HERSHEY_PLAIN,1,(0,0,255),2)
    cv2.rectangle(img, (x, y), (x + 50, y + 50), (0, 0, 255), 2)
    x = x + dx
    y = y + dy
    if x >= 590 or x <= 0:
        dx=dx*(-1)
    if y >= 430 or y <= 0:
        dy = dy*(-1)
    cv2.imshow('Frame', img)
    if cv2.waitKey(20) & 0xff == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()