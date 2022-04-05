import imageio
import cv2
from PIL import Image
import numpy as np



def pre_ani(img1,img2):
    print("Type1", type(img1))
        #Đọc ảnh
    img1 = cv2.imread(img1)
    img2 = cv2.imread(img2)


    #Thay đổi kích thước ảnh theo w,h:
    img1 = cv2.resize(img1,(400,300))
    img2 = cv2.resize(img2,(400,300))
    print("Type 2",type(img1))
    return (img1,img2)


def animation (img1, img2,Speed) :
    img1, img2 = pre_ani(img1,img2)
    h, w = img1.shape

    for D in range(0,h+1,Speed):
    #print(D)
        result = img1.copy()
        result[0:h-D,:,:]=img1[D:h,:,:]
        result[h-D:h,:,:]=img2[0:D,:,:]
        cv2.imshow("Push",result)
        cv2.waitKey(10)

def blend_img(fg, mask,bg) :
    fg = cv2.imread(fg)

    mask = cv2.imread(mask, cv2.IMREAD_UNCHANGED)

    fg= cv2.resize(fg,(400,300))
    mask= cv2.resize(mask,(400,300))

    frames = imageio.mimread(bg, '.gif')

    fg_h, fg_w, fg_c = fg.shape
    bg_h, bg_w, bg_c = frames[0].shape
    top = int((bg_h-fg_h)/2)
    left = int((bg_w-fg_w)/2)
    bgs = [frame[top: top + fg_h, left:left + fg_w, 0:3] for frame in frames]

    results = []
    alpha = 0.8
    for i in range(len(bgs)):
        alpha -= 0.02
        if alpha <= 0:
            alpha = 0
        result = fg.copy()
        result[mask[:,:,3] != 0] = alpha * result[mask[:,:,3] != 0]
        bgs[i][mask[:,:,3] == 0] = 0
        bgs[i][mask[:,:,3] != 0] = (1-alpha)*bgs[i][mask[:,:,3] != 0]
        result = result + bgs[i]
        results.append(result)
    return results

def aniblend (fg1,mask1,bg1,fg2,mask2,bg2,Speed):
    img1, img2 = pre_ani(fg1,fg2)

    frame_1 = blend_img(fg1,mask1,bg1)
    frame_2 = blend_img(fg2,mask2,bg2)

    h, w, _ = img1.shape
    result_push = []
    result_wide = []
    result_uncover = [] 
    min_len = min(len(frame_1),len(frame_2))
    print("min_len",min_len)
    result_final = []
    for D in range(0,h+1,Speed) :
        X = D%min_len
        result = frame_1[X].copy()
        result[0:h-D,:,:]=frame_1[X][D:h,:,:]
        result[h-D:h,:,:]=frame_2[X][0:D,:,:]
        result_push.append(result)

    for D in range(0,w+1,Speed):
        X = D%min_len

        result = frame_1[X].copy()
        result[:,0:D,:]=frame_1[X][:,w-D:w,:]
        result[:,D:w,:]=frame_2[X][:,0:w-D]
        result_wide.append(result)

    for D in range(0,w+1,Speed):
        X = D%min_len
        result = frame_1[X].copy()
        result[:,0:w-D,:] = frame_1[X][:,D:w,:]
        result[:,w-D:w,:] = frame_2[X][:,w-D:w,:]
        result_uncover.append(result)

    return (result_push, result_wide , result_uncover)


def create_movie(total_frames):
    width = 400
    hieght = 300
    channel = 3

    fps = 30

    fourcc = cv2.VideoWriter_fourcc(*'AVI1')
    video = cv2.VideoWriter('test.avi', fourcc, float(fps), (width, hieght))

    for frame in total_frames:
        for frame_count in range(0,len(frame)):
            img = frame[frame_count]
            video.write(img)
    
    video.release()


result_push, result_wide , result_uncover = aniblend ("meo1.jpg","cat_rm1.png","3.gif","meo2.jpg","cat_rm2.png","3.gif",8)
total_frame = [result_push, result_wide , result_uncover]
create_movie(total_frame)

