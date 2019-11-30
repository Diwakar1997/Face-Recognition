
import cv2
cap=cv2.VideoCapture(0)

id=input("Enter id ")
val=0
name=input("Enter name ")
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    ret,frame=cap.read()

    face=face_cascade.detectMultiScale(frame,1.3,5)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    for x,y,w,h in face:
        val=val+1
        cv2.imwrite("Images/"+str(name)+"."+str(id)+"."+str(val)+".jpg", gray[y:y+h,x:x+w])
        cv2.imshow('image', gray)
    k = cv2.waitKey(100) & 0xff

    if val >= 50:
        break

cap.release()
cv2.destroyAllWindows()

