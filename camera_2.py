import cv2
cap=cv2.VideoCapture(0) # first camera
# to check the camera is opened or not
while True:
    status,frame=cap.read()
    grayimage=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    print(frame.shape)
    #now we can draw all the pattern
    cv2.line(frame,(0,0),(200,300),(0,255,0),3)      # image, point1,point2, colour, thickness
    cv2.rectangle(frame,(50,50),(250,300),(0,0,255),3) # image , point1 , point2 , colour , thickness
    cv2.circle(grayimage,(200,300),100,(123,123,123),2) # image . point1 ,point2 , colour, thickness
    font = cv2.FONT_HERSHEY_SIMPLEX     # font style
    cv2.putText(frame,'adhoc',(10,50),font,2,(0,2,55),2,cv2.LINE_AA)
    cv2.imshow('live',frame)
    cv2.imshow('livegray',grayimage)
    if cv2.waitKey(5) & 0xff == ord('q'):
        break
cv2.destroyAllWindows()
cap.release()