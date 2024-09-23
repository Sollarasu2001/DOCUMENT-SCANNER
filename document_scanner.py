import cv2
import pytesseract
from PIL import Image
import io
import numpy as np

def process_image(image_bytes):
    # Convert image bytes to PIL Image
    image = Image.open(io.BytesIO(image_bytes))

    # Convert PIL Image to OpenCV image
    image_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    # Perform OCR
    text = pytesseract.image_to_string(image_cv)

    return text