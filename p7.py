#!/usr/bin/python
import  cv2
import numpy as np
face_cascade = cv2.CascadeClassifier('C:/Program Files/Python36/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')

cap=cv2.VideoCapture(0)
while True:
	status,img=cap.read()
	grayimg=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(grayimg,1.15,5)  
	for  (x,y,w,h) in faces:
		cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2) 
		roi_gray=grayimg[y:y+h,x:x+w]
		roi_color=img[y:y+h,x:x+w]
			
	cv2.imshow('imgw',img)
	if cv2.waitKey(30) & 0xff == ord('q'):
		break		
cap.release()
cv2.destroyAllWindows()
