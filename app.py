import streamlit as st
import tensorflow as tf
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image

# Load model once
@st.cache_resource
def load_fruit_model():
    return load_model("fruit_quality_detector.h5")


model = load_fruit_model()

# Class names as per training
class_names = ['Fresh', 'Mild', 'Rotten']

# Title
st.title("🍎 Fruit Quality Detector")
st.write("Upload a fruit image and find out if it's **Fresh**, **Mild**, or **Rotten**.")

# Upload image
uploaded_file = st.file_uploader(r"C:\Users\Aditya Reddy\Desktop\mango.jpg", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Load and display image
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image", use_column_width=True)

    # Preprocess image
    img_resized = img.resize((224, 224))
    img_array = image.img_to_array(img_resized)
    img_array = tf.expand_dims(img_array, 0) / 255.0  # Normalize

    # Predict
    predictions = model.predict(img_array)
    predicted_index = np.argmax(predictions)

    if predicted_index < len(class_names):
        predicted_class = class_names[predicted_index]
        confidence = np.max(predictions)

        st.success(f"✅ Predicted: **{predicted_class}**")
        st.info(f"🎯 Confidence: `{confidence:.2f}`")
    else:
        st.error("Prediction index out of range. Check model or class_names.")
