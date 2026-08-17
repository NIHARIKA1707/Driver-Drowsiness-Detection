import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

st.set_page_config(
    page_title="Driver Drowsiness Detection",
    page_icon="🚗"
)

st.title("🚗 Driver Drowsiness Detection")
st.write("Monitor the driver's condition using an image or camera.")

# Load trained CNN model
@st.cache_resource
def load_model():
	return tf.keras.models.load_model("driver_drowsiness_efficientnetb0.keras")
    

model = load_model()

class_names = [
    "closed",
    "open",
    "no_yawn",
    "yawn"
]


def predict_image(image):

    image = image.convert("RGB")
    image = image.resize((224, 224))
	
    image_array = np.array(image)
    image_array = np.expand_dims(image_array, axis=0)

    prediction = model.predict(image_array, verbose=0)

    predicted_class = np.argmax(prediction[0])
    confidence = float(prediction[0][predicted_class])

    return class_names[predicted_class], confidence


st.subheader("📷 Camera")

camera_image = st.camera_input("Take a picture of the driver")

if camera_image is not None:

    image = Image.open(camera_image)

    st.image(
        image,
        caption="Captured Driver Image",
        use_container_width=True
    )

    result, confidence = predict_image(image)

    st.subheader("Detection Result")

    st.write(f"**Detected Class:** {result}")
    st.write(f"**Confidence:** {confidence * 100:.2f}%")

    if result in ["closed", "yawn"]:

        st.error("🔴 DROWSY DETECTED!")

        st.warning(
            "⚠️ Driver may be drowsy. Please take a break."
        )

    else:

        st.success("🟢 DRIVER IS ALERT")

        st.info(
            "Driver appears to be awake."
        )


st.divider()

st.subheader("📁 Or Upload an Image")

uploaded_file = st.file_uploader(
    "Choose a driver image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Driver Image",
        use_container_width=True
    )

    result, confidence = predict_image(image)

    st.subheader("Detection Result")

    st.write(f"**Detected Class:** {result}")
    st.write(f"**Confidence:** {confidence * 100:.2f}%")

    if result in ["closed", "yawn"]:

        st.error("🔴 DROWSY DETECTED!")

        st.warning(
            "⚠️ Driver may be drowsy. Please take a break."
        )

    else:

        st.success("🟢 DRIVER IS ALERT")

        st.info(
            "Driver appears to be awake."
        )