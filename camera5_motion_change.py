import cv2
# start the camera
cap = cv2.VideoCapture(0)

tp1=cap.read()[1] # take 1
tp2=cap.read()[1] # take 2
tp3=cap.read()[1] # take3

# to make more perfect (if light off then we can use this to detection of colour)
gray1=cv2.cvtColor(tp1,cv2.COLOR_BGR2GRAY) # converting into gray
gray2=cv2.cvtColor(tp2,cv2.COLOR_BGR2GRAY) # converting into gray
gray3=cv2.cvtColor(tp3,cv2.COLOR_BGR2GRAY) # converting into gray

# now creating image differentitor
def img_diff(x,y,z):
    #diff between x,y ----gray1 and gray2 -----d1
    d1=cv2.absdiff(x,y)
    #diff between y,z ----gray2 and gray3 ----d2
    d2=cv2.absdiff(y,z)
    # absolute diff d1-d2
    finalimg=cv2.bitwise_and(d1,d2)    # here in this bitwise operation takes place
    return finalimg
# now applying function
while cap.isOpened():
    status, frame=cap.read()
    motion_img=img_diff(gray1,gray2,gray3)
    # replacing image frame
    gray1 = gray2
    gray2 = gray3
    gray3 = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) # passing live image to gray3
    cv2.imshow('motion',frame) # for colour motion
    cv2.imshow('motion',motion_img)
    cv2.waitKey(10) & 0xff==ord('q')
cv2.destroyAllWindows()
cap.release()