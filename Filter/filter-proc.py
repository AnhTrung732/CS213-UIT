import numpy as np
import cv2
import matplotlib.pyplot as plt
from skimage.io import imread, imshow
from skimage.color import rgb2gray
from skimage import img_as_uint
from scipy.signal import convolve2d

#img = imread('c.jpg')
# img = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
#                 [0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
#                 [0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
#                 [0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
#                 [0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
#                 [0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
#                 [0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
#                 [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#                 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],])

img = np.array([[0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
                [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
                [0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25],
                [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5],
                [1, 1, 1, 1, 1, 2, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 2, 1, 1, 1, 1],
                [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5],
                [0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25],
                [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
                [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],])
print(img.shape)

#img_gray = rgb2gray(img)
#imshow(img_gray)
#cv2.imshow('Anh mat', img)

h1_sobel = np.array([[1, 2, 1],
                    [0, 0, 0],
                    [-1, -2, -1]])

h2_sobel = np.array([[-1, -2, -1],
                    [0, 0, 0],
                    [1, 2, 1]])

x = (-convolve2d(img, h1_sobel))
y = (-convolve2d(img, h2_sobel))
print(x)
print(y)
np.savetxt("Anh1.txt",x, fmt='%f')
np.savetxt("Anh2.txt",y, fmt='%f')

