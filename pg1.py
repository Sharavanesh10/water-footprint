import cv2
import pytesseract

# Load an image from file
image = cv2.imread('mee.jpg')

# Convert the image to grayscale for text extraction
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Use Tesseract OCR to extract text from the image
product_name = pytesseract.image_to_string(gray_image)

# Dictionary of hypothetical water footprints for some products (in liters per unit)
water_footprints = {
    "apple": 70,
    "banana": 40,
    "carrot": 24,
    # Add more products and their water footprint values here
}

# Lookup the water footprint for the recognized product
water_footprint = water_footprints.get(product_name.lower(), "Unknown")

if water_footprint == "Unknown":
    print("Product not recognized.")
else:
    print(f"Water footprint for {product_name}: {water_footprint} liters per unit")
