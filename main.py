import cv2
import piexif

def is_photoshopped(image_path):
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply a blur filter to the grayscale image
    blurred = cv2.GaussianBlur(grayscale, (5, 5), 0)

    # Calculate the Laplacian of the blurred image
    laplacian = cv2.Laplacian(blurred, cv2.CV_64F).var()

    # Read exif data
    exif_data = piexif.load(image_path)

    # Extract relevant EXIF tags
    ifd_exif = exif_data.get('Exif', {})
    software_tag = ifd_exif.get(piexif.ExifIFD.Software)
    is_manipulated = software_tag is not None and "photoshop" in software_tag.lower()

    print(" Chance the image is manipulated: " , laplacian, "out of 100")
    print("According to the EXIF data analysis this image is surely edited with software: " , is_manipulated)
    
image_path = "your_image_path"
is_photoshopped(image_path)