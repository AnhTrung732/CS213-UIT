# Redd - Write - Show Image
import cv2
'''
# READ
img = cv2.imread('meo.jpg')
print("Cao %d pixel, rong: %d pixel, %d kenh mau." % (img.shape[0], img.shape[1], img.shape[2]))
#img = cv2.imread('meo.jpg', 0)
'''
'''
# WRITE
img = cv2.imread('meo.jpg')
cv2.imwrite('output.jpg', img)
'''

#SHOW
img = cv2.imread('meo.jpg')
cv2.imshow('Anh meo', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
