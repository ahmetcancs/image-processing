import cv2
import numpy as np
img = cv2.imread('picture1.jpg',0)
img = img/255
cv2.imshow('original image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
x,y = img.shape
g = np.zeros((x,y), dtype=np.float32)
pepper = 0.1
salt = 0.95
for i in range(x):
    for j in range(y):
        rdn = np.random.random()
        if rdn < pepper:
            g[i][j] = 0
        elif rdn > salt:
            g[i][j] = 1
        else:
            g[i][j] = img[i][j]
cv2.imshow('image with noise', g)
cv2.waitKey(0)
cv2.destroyAllWindows()