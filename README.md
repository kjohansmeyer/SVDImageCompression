# SVDImageCompression
Image Compression Using Singular Value Decomposition (Project for Applied Linear Algebra)

BWCompression.py converts an image from color to grayscale, then compresses it to the specified number of modes (singular values).

ColorCompression.py compresses a color image to the specified number of modes.

How to use:
1. Clone/download the repository.
2. Place your image file in the same folder as the cloned repository.
3. Write your image's file name in the following line of code: "img = plt.imread('INSERT FILE NAME HERE')" e.g. "img = plt.imread('file name.png')"
4. Change the number of modes: "modes = 5 # Change number of modes (the more nodes, the higher image quality)"
5. Run the code. By default, the code will show the compressed plot, and save the compressed image.
