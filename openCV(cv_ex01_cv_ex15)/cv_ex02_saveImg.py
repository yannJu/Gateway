import cv2

imageFile = './data/lena.jpg'
img = cv2.imread(imageFile)

#압축
cv2.imwrite('./data/lena.bmp', img)
#png 변환 -> 기본 3으로 압축하는데 9면 매우 압축이 크게 들어감 
cv2.imwrite('./data/lena.png', img)
cv2.imwrite('./data/lena2.png', img, [cv2.IMWRITE_PNG_COMPRESSION, 9])
#jpeg 10 정도 손실 발생
cv2.imwrite('./data/lena2.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 90])