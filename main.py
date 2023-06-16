from flask import Flask, request, jsonify
import cv2
import piexif

app = Flask(__name__)

@app.route("/check-image", methods=["POST"])
def check_image():
    if "image" not in request.files:
        return jsonify({"error": "No image file provided"})

    image_file = request.files["image"]
    image_path = "/path/to/save/uploaded/image.jpg"  # Provide the path where you want to save the uploaded image
    image_file.save(image_path)

    authenticity_result = is_photoshopped(image_path)

    return jsonify(authenticity_result)

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

    authenticity_result = {
        "laplacian": laplacian,
        "is_manipulated": is_manipulated
    }

    return authenticity_result

if __name__ == "__main__":
    app.run()