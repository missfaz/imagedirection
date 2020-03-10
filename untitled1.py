# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 09:58:36 2020

@author: Intern
"""

import numpy
import cv2 
 
img = cv2.imread('holi.jpg') 
 
verticalAppendedImg = numpy.vstack((img,img))
horizontalAppendedImg = numpy.hstack((img,img,img))
 
 
cv2.imshow('Vertical Appended', verticalAppendedImg)
#cv2.imshow('Horizontal Appended', horizontalAppendedImg)
 
cv2.waitKey(0)
cv2.destroyAllWindows()