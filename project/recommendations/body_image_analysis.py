from PIL import Image
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
import cv2
import matplotlib.pyplot as plt

def analyze_body_image(image_path):
    print(f"Debug - Analyzing image from path: {image_path}")

    # Load the image and preprocess it
    image = Image.open(image_path)
    image = image.convert('RGB')
    image = image.resize((224, 224))  # Resize for MobileNetV2 input
    image_array = np.array(image)

    # Preprocess image for MobileNetV2
    image_array = preprocess_input(image_array)
    image_array = np.expand_dims(image_array, axis=0)

    # Load a pre-trained MobileNetV2 model for image classification
    model = MobileNetV2(weights='imagenet')

    # Run the image through the model to get predictions
    predictions = model.predict(image_array)
    decoded_predictions = decode_predictions(predictions, top=3)[0]
    print(f"Debug - Decoded predictions: {decoded_predictions}")

    # Check if the image is of a human body
    is_body_image = any('person' in pred[1].lower() for pred in decoded_predictions)
    if not is_body_image:
        return "The provided image does not appear to be a body photo. Please upload a full-body image for analysis."

    # Perform a detailed health classification based on image features
    body_health_result = perform_health_assessment(image_path)

    return body_health_result

def perform_health_assessment(image_path):
    # Load the image using OpenCV for contour analysis
    image = cv2.imread(image_path)
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect body contour
    contours, _ = cv2.findContours(image_gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    body_contour = max(contours, key=cv2.contourArea) if contours else None

    if body_contour is not None:
        print(f"Debug - Detected body contour area: {cv2.contourArea(body_contour)}")

        # Determine health level based on contour area
        contour_area = cv2.contourArea(body_contour)
        if contour_area > 50000:
            return "The analysis suggests you may have a higher body mass index. Consider a balanced diet and regular exercise to improve overall health."
        elif 20000 < contour_area <= 50000:
            return "Your body shape appears within a typical range. Continue maintaining a healthy lifestyle."
        else:
            return "The analysis indicates a lean body type. Maintain a nutritious diet and strength training to support muscle health."
    else:
        return "Unable to detect a clear body contour in the image. Ensure the photo is well-lit and captures your full body."

# Example usage:
# result = analyze_body_image('path/to/full_body_image.jpg')
# print(result)
