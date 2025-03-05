#demo.py
from scipy.ndimage import convolve
import hw3_helper_utils
from wiener_filtering import *
import numpy as np
from PIL import Image
import cv2
import os
import matplotlib.pyplot as plt


# Get the grayscale image
filename = "input_img.png"

# Read the image into a PIL entity
img = Image.open(fp=filename)

# Keep only the Luminance component of the image
bw_img = img.convert("L")

# 'x' is the input grayscale image, of type float and normalized to [0, 1]
x = bw_img / np.max(bw_img)

# create white noise with level 0.02 or 0.2
noise_level = 0.02
#noise_level = 0.2
v = noise_level * np.random.randn(*x.shape)

# create motion blur filter
h = hw3_helper_utils.create_motion_blur_filter(length=20, angle=30)
#h = hw3_helper_utils.create_motion_blur_filter(length=10, angle=0)

# obtain the filtered image
y0 = convolve(x, h, mode="wrap")

# generate the noisy image
y = y0 + v

# compute x_iv0, x_inv, x_hat
# set a range of K values for testing
K_values = [0.01, 0.1, 1, 10, 100, 1000, 10000]

# experiment with different K values to find the best approximation of x_hat
min_error_x_hat = float('inf')
J_values_x_hat = []

for K in K_values:
    x_hat = my_wiener_filter(y, h, K)
    # mean squared error
    error_x_hat = np.mean((x_hat - x) ** 2) 
    # append it on J_values
    J_values_x_hat.append(error_x_hat)
    # save the best x_hat, x,inv0
    if error_x_hat < min_error_x_hat:
        best_x_hat = x_hat
        min_error_x_hat = error_x_hat
        best_K = K
x_hat = best_x_hat
x_inv = my_wiener_filter(y, h, 1e8)
x_inv0 = my_wiener_filter(y0, h, 1e8)

# plot the images 
fig, axs = plt.subplots(nrows=2, ncols=3, figsize=(12, 7))

axs[0][0].imshow(x, cmap='gray');
axs[0][0].set_title("Original image x")
axs[0][1].imshow(y0, cmap='gray');
axs[0][1].set_title("Clean image y0")
axs[0][2].imshow(y, cmap='gray');
axs[0][2].set_title("Blurred and noisy image y")
axs[1][0].imshow(x_inv0, cmap='gray');
axs[1][0].set_title("Inverse filtering noiseless output x_inv0")
axs[1][1].imshow(x_inv, cmap='gray');
axs[1][1].set_title("Inverse filtering noisy output x_inv")
axs[1][2].imshow(x_hat, cmap='gray');
axs[1][2].set_title("Wiener filtering output x_hat")

fig.suptitle(f"Image with noise level {noise_level}")

plt.show()

# plot the variation of J with respect to K for x_hat
plt.figure(figsize=(10, 5))

plt.plot(K_values, J_values_x_hat , marker='o')
plt.xscale('log')
plt.xlabel('K')
plt.ylabel('J (Mean Squared Error)')
plt.title(f'Variation of J with respect to K around K0={best_K}')
plt.grid(True)

plt.show()
