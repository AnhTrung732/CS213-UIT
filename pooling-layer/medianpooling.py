import cv2
import numpy as np
import matplotlib.pyplot as plt

img = np.array([[1.0108, -0.0721, -0.5277,  0.4403],
                [1.1985, -0.5135,  1.3065, -1.0913],
                [0.7962,  0.8527,  0.4207, -0.0916],
                [0.8412,  0.3495,  0.5528, -0.4201]])

def maxpool(image):
    m = len(image)
    n = len(image[0])
    print(m,n)
    new_image = np.zeros((m//2 + 1, n//2 +1))
    xRows = [1, 1, 0]
    yCols = [0, 1, 1]

    for i in range(0, m, 2):
        for j in range(0, n, 2):
            currentPixels = [image[i][j]]
            for k in range(3):
                neighbor_x = i + xRows[k]
                neighbor_y = j + yCols[k]
                if neighbor_x < m and neighbor_y < n :
                    currentPixels.append(image[neighbor_x][neighbor_y])
                new_image[i//2][j//2] = np.median(currentPixels)
    print(new_image)
    return new_image
    
result3 = maxpool(img)

