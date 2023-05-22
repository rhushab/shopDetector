import cv2

def is_photoshopped(image_path):
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply a blur filter to the grayscale image
    blurred = cv2.GaussianBlur(grayscale, (5, 5), 0)

    # Calculate the Laplacian of the blurred image
    laplacian = cv2.Laplacian(blurred, cv2.CV_64F).var()

    print(" Chance the image is manipulated: " , laplacian, "out of 100")
image_path = "your_image_path"
is_photoshopped(image_path)