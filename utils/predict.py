import tensorflow as tf
import numpy as np
import json

from utils.preprocess import preprocess_image

# load model
model = tf.keras.models.load_model(
    "model/fashion_classifier.h5"
)

# load labels
with open("model/class_indices.json", "r") as f:
    class_indices = json.load(f)
labels = {v: k for k, v in class_indices.items()}


def predict_style(image):

    processed_image = preprocess_image(image)

    prediction = model.predict(processed_image)

    predicted_class = np.argmax(prediction)

    style = labels[predicted_class]

    confidence = prediction[0][predicted_class]

    return style, confidence