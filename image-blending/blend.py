import imageio
import cv2

fg = cv2.imread('face.jpg')

mask = cv2.imread('face_1.png', cv2.IMREAD_UNCHANGED)

fg= cv2.resize(fg,(400,300))
mask= cv2.resize(mask,(400,300))
print(fg.shape)
print(mask.shape)

frames = imageio.mimread("3.gif", '.gif')

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

imageio.mimsave('result.gif', results)
