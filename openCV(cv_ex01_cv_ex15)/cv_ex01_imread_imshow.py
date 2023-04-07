import cv2

imageFile = './data/lena.jpg'
img = cv2.imread(imageFile)
img2 = cv2.imread(imageFile, cv2.IMREAD_GRAYSCALE)

print(img.shape, img2.shape)

cv2.imshow('Lena Color', img)
cv2.imshow('Lena Gray', img2)

cv2.waitKey()