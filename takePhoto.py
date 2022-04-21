import time
import cv2

cap = cv2.VideoCapture(0) # video capture source camera (Here webcam of laptop) 

start = time.time()

while(True):
    ret,frame = cap.read() # return a single frame in variable `frame`
    # cv2.imshow('img1',frame) #display the captured image
    end = time.time()
    if ((end - start) > 0.4):
      cv2.imwrite('./img/mugShot.png',frame)
      break
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #   break


cap.release()
cv2.destroyAllWindows()