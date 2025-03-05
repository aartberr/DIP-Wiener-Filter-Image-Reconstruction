#wiener_filtering.py
import numpy as np
from scipy.fft import fft2, ifft2

# apply the Wiener filter to restore a distorted image y using impulse response h and parameter k
def my_wiener_filter(y, h, K):
    # get the shape of y and h
    M, N = y.shape
    L, P = h.shape
    
    # zero-pad h to the size of the input image
    h_padded = np.pad(h, ((0, M - L), (0, N - P)), 'constant')

    # compute FFT of h response and its conjugate
    H = fft2(h_padded)
    H_conj = np.conj(H)

    # construct Wiener filter
    if K == 0:
        # to avoid division by 0
        K = 1e-8
    H_abs_squared = np.abs(H) ** 2
    
    # to avoid division by 0
    G = H_conj / np.where((H_abs_squared + 1 / K) == 0, 1e-8, H_abs_squared + 1 / K)
    
    # compute FFT of y
    Y = fft2(y)
    
    # apply Wiener filter by pointwise multiplication
    X_hat_freq = G * Y
    
    # compute x_hat from the inverse FFT 
    x_hat = np.real(ifft2(X_hat_freq))

    return x_hat
