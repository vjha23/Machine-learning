import cv2
cap = cv2.VideoCapture(0)    # first camera
# to check camera is started or not
plugin = cv2.VideoWriter_fourcc(*'XVID')  #XVID is plugin  (for avi we use this)  (load plugin)
output = cv2.VideoWriter('class.avi',plugin,24,(640,480))   # filename , plugin, fps,frame_size(resolution)

while cap.isOpened():
    status,frame=cap.read()
    cv2.imshow('live',frame)
    #draw pattern
    output.write(frame)
    if cv2.waitKey(5) & 0xff==ord('q'):
        break
cv2.destroyAllWindows()
cap.release()
