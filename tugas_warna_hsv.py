import cv2
import numpy as np

sumber_gambar = cv2.imread('foto1.jpeg')

gambar_hsv = cv2.cvtColor(sumber_gambar, cv2.COLOR_BGR2HSV)

cv2.namedWindow('Gambar asli', cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)
cv2.namedWindow('Gambar HSV', cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)
    
cv2.resizeWindow('Gambar asli', 600, 600) 
cv2.resizeWindow('Gambar HSV', 600, 600)

cv2.imshow('Gambar asli', sumber_gambar)
cv2.imshow('Gambar HSV', gambar_hsv)

cv2.waitKey(0)
cv2.destroyAllWindows()