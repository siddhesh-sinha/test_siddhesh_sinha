import cv2 as cv
import numpy as np

image = cv.imread('E:\computer\python\lol\oh damn son\Resources\Photos\IP_images\contour.png')
image_HSV = cv.cvtColor(image,cv.COLOR_BGR2HSV)
image_blue,image_green,image_red = cv.split(image)
blank = np.zeros(image.shape[:2],dtype='uint8')
blank_blue = np.zeros(image.shape[:2],dtype='uint8')
blank_green = np.zeros(image.shape[:2],dtype='uint8')
blank_red = np.zeros(image.shape[:2],dtype='uint8')
image_grey = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
blue_pic = cv.merge([image_blue,blank,blank])
red_pic = cv.merge([blank,blank,image_red])
green_pic = cv.merge([blank,image_green,blank])



cv.imshow('initial photo',image)
cv.imshow('photo1',blue_pic)
cv.imshow('photo2',green_pic)
cv.imshow('photo3',red_pic)
cv.waitKey(0)
'''
frame=cv2.imread('E:\computer\python\lol\oh damn son\Resources\Photos\IP_images\contour.png')
img=cv2.resize(frame,(600,600))
kernel = np.ones((5,5),np.uint8)
dilation = cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)
img_hsv=cv2.cvtColor(dilation, cv2.COLOR_BGR2HSV)
lower_red = np.array([0,150,50])
upper_red = np.array([10,255,255])
mask_red = cv2.inRange(img_hsv, lower_red, upper_red)
contours, hierarchy = cv2.findContours(mask_red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for contour in contours:
    area = cv2.contourArea(contour)
    if (area > 300):
        x, y, w, h = cv2.boundingRect(contour)
        imageFrame = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

        cv2.putText(img, "Red Colour", (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1.0, (255, 243, 0))

cv2.imshow("HSV", img_hsv)
cv2.imshow("Image", imageFrame)

while (True):
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cv.waitKey(0)'''