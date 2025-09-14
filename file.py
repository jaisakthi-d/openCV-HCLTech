import numpy as np
import cv2

# Create a synthetic 100x100 grayscale image with noise
np.random.seed(42)
image = np.ones((100, 100), dtype=np.uint8) * 128  # Base gray image
image[40:60, 40:60] = 255  # Add a white square (text-like feature)
noise = np.random.normal(0, 25, image.shape).astype(np.uint8)
noisy_image = np.clip(image + noise, 0, 255).astype(np.uint8)

# Simple averaging filter (3x3 kernel)
def simple_averaging(image):
    kernel = np.ones((3, 3), dtype=np.float32) / 9
    return cv2.filter2D(image, -1, kernel)

# Gaussian kernel filter (3x3 kernel, sigma=1)
def gaussian_filter(image):
    kernel = np.array([[1, 2, 1],
                       [2, 4, 2],
                       [1, 2, 1]], dtype=np.float32) / 16  # Gaussian kernel
    return cv2.filter2D(image, -1, kernel)

# Apply filters
simple_avg_result = simple_averaging(noisy_image)
gaussian_result = gaussian_filter(noisy_image)

# Calculate Mean Squared Error (MSE) to compare with original clean image
def mse(image1, image2):
    return np.mean((image1.astype(float) - image2.astype(float)) ** 2)

mse_simple = mse(image, simple_avg_result)
mse_gaussian = mse(image, gaussian_result)

# Save images for visual comparison
cv2.imwrite('noisy_image.png', noisy_image)
cv2.imwrite('simple_avg_image.png', simple_avg_result)
cv2.imwrite('gaussian_image.png', gaussian_result)


# Display images (optional, for environments supporting display)
cv2.imshow('Noisy Image', noisy_image)
cv2.imshow('Simple Averaging', simple_avg_result)
cv2.imshow('Gaussian Filter', gaussian_result)
