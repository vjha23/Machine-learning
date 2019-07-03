import cv2
# starting the camera
cap = cv2.VideoCapture(0) # 0 means face cam
# status of camera
while cap.isOpened():
    status,frame = cap.read()
    # detecting the red colour
    redimg = cv2.inRange(frame,(0,0,0),(40,40,255))
    cv2.imshow('livered colour ',redimg)
    if cv2.waitKey(5) & 0xff==ord('q'):
        break
cv2.destroyAllWindows()
cap.release()