import numpy as np
import cv2
import matplotlib.pyplot as plt
'''
# HIEN THI ANH
img = cv2.imread('meo.jpg',0)
print(type(img))
print(img.shape)
plt.imshow(img, cmap='gray')
plt.show()
'''

'''
# 1. lAY KICH THUOC ANH
(h, w, d) = img.shape
print("width={}, height={}, depth{}".format(w, h, d))

# 2. LAY GIA TRI MAU MOT DIEM ANH 
#Ta lấy pixel/điểm ảnh tại vị trí w=50, h=50, d=0
(B, G, R) = img[50, 50]
print("R={}, G={}, B={}".format(R, G, B))
'''

'''
# 3. XOAY ANH THEO CHIEU DOC
img = cv2.imread('meo.jpg',0)
result = img[::-1,:]
plt.imshow(result, cmap='gray')
plt.show()
'''
'''
# 4. XOAY ANH THEO DUONG CHEO CHINH
img = cv2.imread('meo.jpg',0)
result1 = img.transpose()
plt.imshow(result1,cmap='gray')
plt.show()
'''
'''
# 5. XOAY ANH THEO CHIEU NGANG
img = cv2.imread('meo.jpg',0)
result = img[:,::-1]
plt.imshow(result,cmap='gray')
plt.show()
'''
'''
# 5. DIEU CHINH SANG TOI CUA ANH
img = cv2.imread('meo.jpg',0)
result = img.copy()
result = result + 50
plt.imshow(result, cmap='gray')
plt.show()
'''
# 6. DOI MAU VUNG ANH
img = cv2.imread('meo.jpg',0)
result = img.copy()
result[100:250, 300:450] = 0
plt.imshow(result,cmap='gray')
plt.show()

