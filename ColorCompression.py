# ========================================================================== #
#                       Created by Kevin Johansmeyer                         #   
# Purpose: Compresses a color image file using Singular Value Decomposition  # 
# (SVD) by truncation                                                        #
#                                                                            #
# Note: Running the program takes ~60 seconds (dependent on file size)       #
# ========================================================================== #

import numpy as np
from matplotlib import pyplot as plt

# ====================== Convert Image Into Matrix ========================= #
# Place image in same directory at this Python file:
img = plt.imread('INSERT FILE NAME HERE')
modes = 20 # Change number of modes (the more nodes, the higher image quality)

# ======================= Size and Shape of Matrix ========================= #
print('Original Matrix Shape:',img.shape)
print('Original Matrix Size:',img.size)
M = img.shape[0] # number of pixels (height)
N = img.shape[1] # number of pixels (width)

# ============================== Red Channel =============================== #
imgRed = np.zeros((M,N))

for m in range (0,M):
    for n in range (0,N):
        imgRed[m][n] = img[m][n][0]

redV, redSigmaVals, redWAdjoint = np.linalg.svd(imgRed, full_matrices=True)

redTruncV = redV[:,:modes]
print(redTruncV.shape)
print(redTruncV.shape)
redTruncSigmaVals = redSigmaVals[:modes]
redTruncSigma = np.diag(redTruncSigmaVals)
redTruncWAdjoint = redWAdjoint[:modes]

redTruncImg = redTruncV @ redTruncSigma @ redTruncWAdjoint
print(redTruncImg.shape) # Recovers M x N dimensions
# ============================ Green Channel =============================== #
imgGreen = np.zeros((M,N))

for m in range (0,M):
    for n in range (0,N):
        imgGreen[m][n] = img[m][n][1]
        
greenV, greenSigmaVals, greenWAdjoint = np.linalg.svd(imgGreen, full_matrices=True)

greenTruncV = greenV[:,:modes]
greenTruncSigmaVals = greenSigmaVals[:modes]
greenTruncSigma = np.diag(greenTruncSigmaVals)
greenTruncWAdjoint = greenWAdjoint[:modes]

greenTruncImg = greenTruncV @ greenTruncSigma @ greenTruncWAdjoint
print(greenTruncImg.shape) # Recovers M x N dimensions
# ============================== Blue Channel ============================== #
imgBlue = np.zeros((M,N))

for m in range (0,M):
    for n in range (0,N):
        imgBlue[m][n] = img[m][n][2]

blueV, blueSigmaVals, blueWAdjoint = np.linalg.svd(imgBlue, full_matrices=True)

blueTruncV = blueV[:,:modes]
blueTruncSigmaVals = blueSigmaVals[:modes]
blueTruncSigma = np.diag(blueTruncSigmaVals)
blueTruncWAdjoint = blueWAdjoint[:modes]

blueTruncImg = blueTruncV @ blueTruncSigma @ blueTruncWAdjoint
print(blueTruncImg.shape) # Recovers M x N dimensions
# ===================== Construct Truncated Matrix ========================= #
constructTruncImg = np.zeros((M,N,3))

for m in range (0,M):
    for n in range (0,N):
        constructTruncImg[m][n][0] = int(redTruncImg[m][n])
        constructTruncImg[m][n][1] = int(greenTruncImg[m][n])
        constructTruncImg[m][n][2] = int(blueTruncImg[m][n])

# Some integer values were not in range of [0,255] which resulted in clipping.
# Suggestion from Dr. Forgoston to scaled all the values using the code:
#scaledConstructImg = np.array(constructTruncImg/np.amax(constructTruncImg)*255, np.int32)
scaledConstructImg = np.array(constructTruncImg/np.amax(constructTruncImg)*255, np.uint8)

# print(constructTruncImg.shape)
# print(constructTruncImg)

plt.imshow(scaledConstructImg)
plt.title('SVD, modes = {}'.format(modes))
plt.show()
plt.imsave('ColorImageCompressed.png', scaledConstructImg)
