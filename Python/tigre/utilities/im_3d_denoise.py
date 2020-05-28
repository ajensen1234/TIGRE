import numpy as np
from _tvdenoising import tvdenoise

def im3ddenoise(img,iter=50,lmbda=15.0, gpuids=None):
    imgmin = np.amin(img.ravel())
    img = img-imgmin
    imgmax = np.amax(img.ravel())
    img = img/imgmax

    img = tvdenoise(img,iter,lmbda,gpuids)

    img*=imgmax
    img+=imgmin

    return img