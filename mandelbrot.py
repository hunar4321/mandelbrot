# a simple Mandelbrot in python (slow)

import numpy as np
import matplotlib.pylab as plt

atoms=[]
window_size = 300
center = window_size/2

mat = np.zeros((window_size, window_size))
for y in range(window_size):
    for x in range(window_size):
        dx = (x-center)/1000-0.12
        dy = (y-center)/1000-0.82
        a = dx
        b = dy
        for t in range(50):
            d = (a*a)-(b*b)+dx
            b = 2*(a*b)+dy
            a = d
            H = d > 200
            if(H==True):
                mat[y, x] = t

plt.imshow(mat)
