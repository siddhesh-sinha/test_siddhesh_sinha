import cv2 as cv

# read image as grey scale
img = cv.imread('E:\computer\python\lol\oh damn son\Resources\Photos/baground.jpg')
img = cv.resize(img,(1280,720))
grey_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
HSV_img = cv.cvtColor(img,cv.COLOR_BGR2HSV)
save = cv.imwrite('E:\computer\python\lol\oh damn son\Resources\Baground_greyscale.jpg', grey_img)
print("Image written to file-system : ", save)
save = cv.imwrite('E:\computer\python\lol\oh damn son\Resources\Baground_HSV.jpg', HSV_img)
print("Image written to file-system : ", save)
