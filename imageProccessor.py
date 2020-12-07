import cv2
import numpy as np

im = cv2.imread("/home/pi/Pictures/1.jpg")
cv2.imshow("image",im);
cv2.waitKey(0)

##show gray image
#gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
#cv2.imshow("gray.jpg", gray)
#cv2.waitKey(0)

#BGR 
#(B, G, R) = cv2.split(im)
#cv2.imshow("Red", R)
#cv2.imshow("Green", G)
#cv2.imshow("Blue", B)
#cv2.waitKey(0)

#flip
#rows, cols, channel = im.shape
#M = cv2.getRotationMatrix2D(((cols-1)/2.0, (rows-1)/2.0), 90, 1)
#dst = cv2.warpAffine(im, M, (cols, rows))
#cv2.imshow("dst", dst)
#dst = cv2.flip(im, 1)   
#cv2.imshow("dst", dst)
#dst = cv2.flip(im, 0)   
#cv2.imshow("dst", dst)
#dst = cv2.flip(im, -1)  
#cv2.imshow("dst", dst)
#cv2.waitKey(0)

#res = cv2.resize(im, None, fx=2, fy=0.5, interpolation = cv2.INTER_CUBIC)
#cv2.imshow("res", res)
#cv2.waitKey(0)

#im1 = im[200:500, 300:600]  #(y0:y1, x0:x1)
#cv2.imshow("im1", im1)
#cv2.waitKey(0)

#res1 = np.uint8(np.clip(1.5*im,0,255))
#res2 = np.uint8(np.clip(0.7*im,0,255))
#tmp1 = np.hstack((im, res1, res2))
#cv2.imshow("image", tmp1)

#gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
#equalize = cv2.equalizeHist(gray)
#cv2.imshow('equalize', equalize)

#blur = cv2.blur(im, (5,5))                      
#gauss = cv2.GaussianBlur(im, (5,5), 0)          
#median = cv2.medianBlur(im, 5)                  
#bilateral = cv2.bilateralFilter(im, 9, 5, 5)    
#filt = np.hstack([blur, gauss, median, bilateral])
#cv2.imshow("filter", filt)

#gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
#_ ,binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
#con=cv2.Canny(binary, 50, 150)
#contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#con = cv2.drawContours(im,contours,-1,(0,0,255),3)
#cv2.imshow("con", con)

gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
dst = cv2.cornerHarris(gray,5,5,0.04)
dst = cv2.dilate(dst,None)
im[dst>0.01*dst.max()]=[0,0,255]
cv2.imshow('dst',im)

cv2.waitKey(0)
