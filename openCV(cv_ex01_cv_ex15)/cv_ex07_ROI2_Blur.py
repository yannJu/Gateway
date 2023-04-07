# 설정한 블록크기(N 으로 나눈) 만큼을 평균화한 값을 입력함으로서 모자이크 처리
import cv2
import numpy as np

src = cv2.imread('./data/lena.jpg', cv2.IMREAD_GRAYSCALE)
# src = cv2.imread('./image.jpeg', cv2.IMREAD_GRAYSCALE)
dst = np.zeros(src.shape, dtype = src.dtype)

N = 64 # 2의 N 승
height, width = src.shape

h = height // N
w = width // N

for i in range(N):
    for j in range(N):
        y = i * h
        x = j * w
        roi = src[y:y + h, x:x + w]
        dst[y:y + h, x:x + w] = cv2.mean(roi)[0]
        # dst[y:y + h, x:x + h] = cv2.mean(roi)[0:3] #Color
        
cv2.imshow("Blur", dst)
cv2.waitKey()
cv2.destroyAllWindows()