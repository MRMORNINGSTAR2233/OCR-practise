import cv2
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import os
def preprocess_image(image_path: str) -> Image:

    image = Image.open(image_path)
    # Convert the PIL image to a numpy array
    image_np = np.array(image)

    # Convert the image to grayscale using OpenCV
    gray = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)
    denoised = cv2.fastNlMeansDenoising(gray, None, 18, 4, 20)
    binary = cv2.adaptiveThreshold(denoised, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                cv2.THRESH_BINARY, 11, 2)
    
    # Step 5: Find Contours for Bounding Boxes
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Step 6: Draw Bounding Boxes and Save Extracted Regions
    output_image = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    extracted_regions = []

    for i, contour in enumerate(contours):
        x, y, w, h = cv2.boundingRect(contour)
        if 20 < w < 200 and 20 < h < 200:  # Adjust size thresholds as needed
            cv2.rectangle(output_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            roi = binary[y:y+h, x:x+w]
            extracted_regions.append(roi)
            roi_path = os.path.join('binary',f"extracted_region_{i}.png")
            cv2.imwrite(roi_path, roi)
            
    cv2.imwrite("output_with_bounding_boxes.png", output_image)
    return cv2.imwrite('ouput.png',binary)

binary = preprocess_image('NAGRAJA BHAT SMVITM-20250202T164531Z-001/NAGRAJA BHAT SMVITM/TP120_S927-CNR/P-07-F.tif')
