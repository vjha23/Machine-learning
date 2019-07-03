import cv2
import matplotlib.pyplot as plt

#checking version of cv2
print(cv2.__version__)
#image reading
#               image_name   iamge property
img = cv2.imread('demo.jpg',1)
img1 = cv2.imread('demo.jpg',0)
img2 = cv2.imread('demo.jpg',-1)
# here 1 means in same colour channel  --RGB or --BGR
# here 0 means is no colour channel  ---- black or white or grey
# here -1 means to maintain the image transparency
print(img)
# shape printing
print(img.shape)
# type printing
#print(type.img)
# to display image
cv2.imshow('image1',img[0:130,1:150])
cv2.imshow('image2',img1)
cv2.imshow('image3',img2)
#wait for window to close
cv2.waitKey(0)   # 0 holds the window unless any key press

cv2.destroyAllWindows()