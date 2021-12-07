import numpy as np
import scipy
import matplotlib.pyplot as plt
import cv2

'''
get_synthetic_data: Returns C, a 2d numpy array representing Hi-C data and
    t, a list of two-element tuples representing boundaries, [(t0, t1),(t1,t2),....]

n - size of Hi-C data
K - number of domains
'''
def get_synthetic_data(n, K):
    C = np.zeros((n, n))
    r = list(range(4, n-1))
    bounds = np.sort(np.random.choice(r, K-1, replace=False))
    bounds = np.append(bounds, 100)
    shift = 0
    t = []
    for i in range(K):
        if i == 0:
            w = bounds[0]
        else:
            w = bounds[i] - bounds[i-1]
        w = 2*(w // 2) - 1
        if w == -1:
            w = 3
        a = cv2.getGaussianKernel(int(w), -1)
        kernel = np.matmul(a, a.T)
        C[shift:shift+w,shift:shift+w] = kernel
        shift += w
        t.append((shift-w, shift))
    return C, t

#n = 100
#K = 9
#C, t = get_synthetic_data(n, K)