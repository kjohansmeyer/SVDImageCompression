# ========================================================================== #
#                       Created by Kevin Johansmeyer                         #   
# Purpose: Convert image to grayscale, then compress image file using        #
# Singular Value Decomposition (SVD) by truncation                           #
#                                                                            #
# Note: Running the program takes ~30 seconds (dependent on file size)       #
# ========================================================================== #

import numpy as np
from matplotlib import pyplot as plt

# ====================== Convert Image Into Matrix ========================= #
# Place image in same directory at this Python file:
img = plt.imread('INSERT FILE NAME HERE')
modes = 5 # Change number of modes (the more nodes, the higher image quality)


# ======================= Size and Shape of Matrix ========================= #
print('Original Matrix Shape:',img.shape)
print('Original Matrix Size:',img.size)
M = img.shape[0] # number of pixels (height)
N = img.shape[1] # number of pixels (width)

# ============================ Reshaping Data ============================== #
# Convert M x N x 3 matrix into M x N using RGB weights from NTSC:
imgBW = np.zeros((M,N))
        
for m in range (0,M):
    for n in range (0,N):
        # RBG weights from NTSC: 0.2989 ∙ Red + 0.5870 ∙ Green + 0.1140 ∙ Blue
        imgBW[m][n] = (0.2989)*img[m][n][0] + (0.5870)*img[m][n][1] + (0.1140)*img[m][n][2]
        
# ========== Uncomment Block to See Uncompressed, Grayscale Image ========== #
# # Constructs new image
# plt.imshow(imgBW, cmap='gray')
# plt.show()
# plt.imsave('BWImage.png', imgBW, cmap='gray')
# ========================================================================== #

# ========================== Compress Using SVD ============================ #
# Documentation: https://numpy.org/doc/stable/reference/generated/numpy.linalg.svd.html
V, sigmaVals, wAdjoint = np.linalg.svd(imgBW, full_matrices=True)

print('V shape:', V.shape)
print('sigmaVals shape:', sigmaVals.shape)
print('w* shape:', wAdjoint.shape)

# =========================== Reconstruct imgBW ============================ #
# simgaVals.shape = (1536,) [needs to be M x N with values on diagonal]

# ============= Uncomment Block to See Reconstruction of imgBW ============= #
# squareSigma = np.diag(sigmaVals)
# if M < N:
#     extraZeros = np.zeros((M,N-M))
#     sigma = np.hstack((squareSigma,extraZeros))
# elif M > N:
#     extraZeros = np.zeros((M-N,N))
#     sigma = np.vstack((squareSigma,extraZeros))

# print('sigma shape:', sigma.shape)


# # Reconstruct by using: V @ sigma @ wAdjoint
# reconstructImg = V @ sigma @ wAdjoint
# print(reconstructImg.shape)
# ========================================================================== #

# ================== Truncate Matrices for Compression ===================== #
truncV = V[:,:modes]
truncSigmaVals = sigmaVals[:modes]
truncSigma = np.diag(truncSigmaVals)
truncWAdjoint = wAdjoint[:modes]
print(truncV.shape)
print(truncSigmaVals.shape)
print(truncWAdjoint.shape)

# ======================= Construct Truncated imgBW ======================== #
constructTruncImg = truncV @ truncSigma @ truncWAdjoint
plt.imshow(constructTruncImg, cmap='gray')
plt.title('SVD, modes = {}'.format(modes))
plt.show()
plt.imsave('BWImageCompressed.png', constructTruncImg, cmap='gray')
