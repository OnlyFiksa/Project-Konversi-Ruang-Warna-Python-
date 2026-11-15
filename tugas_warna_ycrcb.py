import cv2
import numpy as np

gambar_asli = cv2.imread('foto5.jpeg')

gambar_ycrcb = cv2.cvtColor(gambar_asli, cv2.COLOR_BGR2YCrCb)

cv2.namedWindow('Gambar asli', cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)
cv2.namedWindow('Gambar YCrCb', cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)
    
cv2.resizeWindow('Gambar asli', 600, 600) 
cv2.resizeWindow('Gambar YCrCb', 600, 600)

cv2.imshow('Gambar asli', gambar_asli)
cv2.imshow('Gambar YCrCb', gambar_ycrcb)

cv2.waitKey(0)
cv2.destroyAllWindows()