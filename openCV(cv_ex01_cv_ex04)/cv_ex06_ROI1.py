import cv2

img = cv2.imread('./data/lena.jpg', cv2.IMREAD_GRAYSCALE)
img[120, 200] = 0
print(img[100:110, 200:210])

img[100:400, 200:300] = 0

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()