# Image Manipulation Detection using OpenCV

This Python program utilizes the OpenCV library to detect the probability of image manipulation. The detection is based on the variance of the Laplacian filter applied to the image.

## Prerequisites

Before running the program, ensure that you have the following dependencies installed:

- Python 3.x
- OpenCV library (`pip install opencv-python`)
- piexif (pip install piexif)

## Usage

1. Place the image you want to analyze in a location accessible to the program.
2. Open the Python script file (`main.py`) in a text editor or an integrated development environment (IDE).
3. Modify the `image_path` variable in the script to specify the path to your image file.
4. Save the changes made to the script.
5. Run the script using the Python interpreter (`main.py`).
6. The program will output the probability of image manipulation as a percentage.

## Understanding the Algorithm

The algorithm used in this program follows these steps:

1. Read the image using the `cv2.imread()` function.
2. Convert the image to grayscale using the `cv2.cvtColor()` function.
3. Apply a blur filter to the grayscale image using the `cv2.GaussianBlur()` function.
4. Calculate the Laplacian of the blurred image using the `cv2.Laplacian()` function.
5. Compute the variance of the Laplacian using the `var()` method.
6. Read the EXIF data of the image using the load function from the piexif library.
7. Extract the relevant EXIF tags, specifically the Software tag, from the Exif IFD.
8. Check if the Software tag exists and if it contains the term "photoshop" (case- insensitive), indicating image manipulation.
9. Print the probability of manipulation based on the Laplacian variance and indicate whether the image is edited with specific software based on the EXIF analysis.

The higher the variance of the Laplacian, the higher the probability that the image has undergone some form of manipulation.

## Example Output

Chance the image is manipulated: 2311.381093137254 out of 100

In the above example, the computed variance of the Laplacian is 2311.381093137254, indicating a relatively high probability of image manipulation.

## Note

- It is important to note that this program does not provide a definitive answer regarding image manipulation. It only offers a probability based on the applied algorithm.
- Ensure that the image you provide as input exists in the specified path and is supported by OpenCV.
- Different types of image manipulations may produce different results, and false positives or false negatives are possible.
- This program should be used as a tool to assist in image analysis, but additional techniques and expert judgment may be necessary for accurate and conclusive results.
