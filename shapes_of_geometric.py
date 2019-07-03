import cv2
import numpy as np

def main():
    img1=np.zeros((600,600,3),np.uint8)
    cv2.line(img1, (300,200),(267,378),(255,0,0),2)
    cv2.rectangle(img1,(200,50),(400,290),(0,255,0),4)
    cv2.circle(img1,(120,120),90,(0,0,250),6)
    cv2.ellipse(img1,(200,300),(40,50),10,20,360,(127,127,127),-1)



    cv2.imshow('image',img1)
    cv2.waitKey(0)
    cv2.destroyWindow('image')

if __name__ == "__main__":
    main()