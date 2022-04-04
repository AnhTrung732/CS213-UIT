import cv2
import os
#Đọc ảnh
img1 = cv2.imread(r'meo1.jpg')
img2 = cv2.imread(r'meo2.jpg')
#Xuất Ảnh ra màn hình:
#cv2.imshow("Anh 1",img1)
#cv2.imshow("Anh 2",img2)
#cv2.waitKey(0)

#lấy kích thước của ảnh:
h1,w1,c1 = img1.shape
h2,w2,c2 = img2.shape

#Lưu vào h chiều cao, w chiều rộng nhỏ nhất giữa 2 ảnh:
h=min(h1,h2)
w=min(w1,w1)

#Thay đổi kích thước ảnh theo w,h:
img1 = cv2.resize(img1,(w,h))
img2 = cv2.resize(img2,(w,h))

## PUSH 
Speed = 5
for D in range(0,h+1,Speed):
    #print(D)
    result=img1.copy()
    result[0:h-D,:,:]=img1[D:h,:,:]
    result[h-D:h,:,:]=img2[0:D,:,:]
    cv2.imshow("Push",result)
    cv2.waitKey(10)

## WIDE
Speed = 6
for D in range(0,w+1,Speed):
    result=img1.copy()
    result[:,0:D,:]=img1[:,w-D:w,:]
    result[:,D:w,:]=img2[:,0:w-D]
    cv2.imshow("FL",result)
    cv2.waitKey(10)

## UNDERCOVER
Speed = 6
for D in range(0,w+1,Speed):
    result=img1.copy()
    result[:,0:w-D,:] = img1[:,D:w,:]
    result[:,w-D:w,:] = img2[:,w-D:w,:]
    cv2.imshow("Uncover",result)
    cv2.waitKey(10)