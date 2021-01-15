
import cv2

# read image as grey scale
grey_img = cv2.imread('/path/to/img', cv2.IMREAD_GRAYSCALE)

# save image
save = cv2.imwrite('/path/to/img.png', grey_img)

print("Image written to file-system : ", save)