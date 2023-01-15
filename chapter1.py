# Import ImageIO
import imageio

# Load "chest-220.dcm"
im = imageio.imread("chest-220.dcm")

# Print image attributes
print('Image type:', type(im))
print('Shape of image array:', im.shape)

-------------------------

# Import ImageIO and load image
imprt imageio
im = imageio.imread("chest-220.dcm")

# Print the available metadata fields
print(im.meta.keys())

----------------------------
# Import ImageIO and PyPlot 
import imageio
import matplotlib.pyplot as plt

# Read in "chest-220.dcm"
im = imageio.imread("chest-220.dcm")

# Draw the image in grayscale & greater contrast
plt.imshow(im,vmin=-200 , vmax=200, cmap='gray')

plt.axis('off')

# Render the image
plt.show()

----------------------------
# Import ImageIO and NumPy
import imageio
import numpy as np

# Read in each 2D image
im1 = imageio.imread('chest-220.dcm')
im2 =  imageio.imread('chest-221.dcm')
im3 =  imageio.imread('chest-222.dcm')

# Stack images into a volume
vol = np.stack([im1,im2,im3],axis=0)
print('Volume dimensions:', vol.shape)

----------------------------
# Import PyPlot
import matplotlib.pyplot as plt

# Initialize figure and axes grid
fig, axes =  plt.subplots(nrows=2, ncols=1)

# Draw an image on each subplot
axes[0].imshow(im1 ,cmap='gray')
axes[1].imshow(im2 ,cmap='gray')

# Remove ticks/labels and render
axes[0].axis('off')
axes[1].axis('off')
plt.show()

----------------------------
# Select frame from "vol"
im1 = vol[:, 256, :]
im2 = vol[:, :, 256]

# Compute aspect ratios
d0, d1, d2 = vol.meta['sampling']
asp1 = d0 / d2
asp2 = d0 / d1

# Plot the images on a subplots array 
fig, axes = plt.subplots(nrows=2, ncols=1)
axes[0].imshow(im1, cmap='gray', aspect=asp1)
axes[1].imshow(im2, cmap='gray', aspect=asp2)
plt.show()
