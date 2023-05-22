# Image Manipulation Detection using OpenCV

This Python program utilizes the OpenCV library to detect the probability of image manipulation. The detection is based on the variance of the Laplacian filter applied to the image.

## Prerequisites

Before running the program, ensure that you have the following dependencies installed:

- Python 3.x
- OpenCV library (`pip install opencv-python`)

## Usage

1. Place the image you want to analyze in a location accessible to the program.
2. Open the Python script file (`image_manipulation_detection.py`) in a text editor or an integrated development environment (IDE).
3. Modify the `image_path` variable in the script to specify the path to your image file.
4. Save the changes made to the script.
5. Run the script using the Python interpreter (`python image_manipulation_detection.py`).
6. The program will output the probability of image manipulation as a percentage.

## Understanding the Algorithm

The algorithm used in this program follows these steps:

1. Read the image using the `cv2.imread()` function.
2. Convert the image to grayscale using the `cv2.cvtColor()` function.
3. Apply a blur filter to the grayscale image using the `cv2.GaussianBlur()` function.
4. Calculate the Laplacian of the blurred image using the `cv2.Laplacian()` function.
5. Compute the variance of the Laplacian using the `var()` method.
6. Print the probability of image manipulation as a percentage.

The higher the variance of the Laplacian, the higher the probability that the image has undergone some form of manipulation.

## Example Output

Chance the image is manipulated: 2311.381093137254 out of 100

In the above example, the computed variance of the Laplacian is 2311.381093137254, indicating a relatively high probability of image manipulation.

## Note

- It is important to note that this program does not provide a definitive answer regarding image manipulation. It only offers a probability based on the applied algorithm.
- Different types of image manipulations may produce different results, and false positives or false negatives are possible.
- This program should be used as a tool to assist in image analysis, but additional techniques and expert judgment may be necessary for accurate and conclusive results.

Feel free to customize the program according to your specific needs and requirements.
