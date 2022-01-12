# SVDImageCompression
Image Compression Using Singular Value Decomposition (Project for Applied Linear Algebra)

BWCompression.py converts an image from color to grayscale, then compresses it to the specified number of modes (singular values).

ColorCompression.py compresses a color image to the specified number of modes.

Example before compression:

![Screenshot 2022-01-12 10 04 25 AM](https://user-images.githubusercontent.com/80725783/149165971-fb1b2eed-2b0c-4e13-835c-406a51c017c3.png)

Example after compression:

![Screenshot 2022-01-12 10 03 59 AM](https://user-images.githubusercontent.com/80725783/149165972-38030a3b-45cc-46f1-971e-e70a260dc1c6.png)

How to use:
1. Clone/download the repository.
2. Place your image file in the same folder as the cloned repository.
3. Write your image's file name in the following line of code: "img = plt.imread('INSERT FILE NAME HERE')" e.g. "img = plt.imread('file name.png')"
4. Change the number of modes: "modes = 5 # Change number of modes (the more nodes, the higher image quality)"
5. Run the code. By default, the code will show the compressed plot, and save the compressed image.
