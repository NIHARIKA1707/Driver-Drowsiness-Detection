import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

st.set_page_config(
    page_title="Driver Drowsiness Detection",
    page_icon="🚗",
    layout="wide"
)

# ---------- Styling ----------
st.markdown("""
<style>
.main-title {
    text-align: center;
    color: #1f4e79;
    font-size: 42px;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    color: #666;
    font-size: 18px;
}

.alert-box {
    padding: 20px;
    border-radius: 12px;
    background-color: #ffe5e5;
    border-left: 6px solid #e53935;
    font-size: 20px;
}

.safe-box {
    padding: 20px;
    border-radius: 12px;
    background-color: #e8f5e9;
    border-left: 6px solid #43a047;
    font-size: 20px;
}
</style>
""", unsafe_allow_html=True)


# ---------- Title ----------
st.markdown(
    '<div class="main-title">🚗 Driver Drowsiness Detection</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">AI-Based Driver Monitoring and Road Safety Assistance</div>',
    unsafe_allow_html=True
)

st.write("")


# ---------- Load EfficientNet-B0 ----------
@st.cache_resource
def load_model():
    return tf.keras.models.load_model(
        "driver_drowsiness_efficientnetb0.keras"
    )


model = load_model()


# ---------- Class Names ----------
class_names = [
    "closed",
    "open",
    "no_yawn",
    "yawn"
]


# ---------- Prediction Function ----------
def predict_image(image):

    image = image.convert("RGB")
    image = image.resize((224, 224))

    image_array = np.array(image)
    image_array = np.expand_dims(image_array, axis=0)

    prediction = model.predict(image_array, verbose=0)

    predicted_index = np.argmax(prediction[0])
    confidence = float(prediction[0][predicted_index]) * 100

    predicted_class = class_names[predicted_index]

    return predicted_class, confidence


# ---------- Input ----------
st.subheader("📷 Driver Monitoring")

uploaded_file = st.file_uploader(
    "Upload a driver image",
    type=["jpg", "jpeg", "png"]
)

st.write("### 📸 Or Use Camera")

camera_image = st.camera_input(
    "Take a picture of the driver"
)


# ---------- Select Input ----------
input_image = None
input_source = None

if camera_image is not None:
    input_image = Image.open(camera_image)
    input_source = "Camera"

elif uploaded_file is not None:
    input_image = Image.open(uploaded_file)
    input_source = "Uploaded Image"


# ---------- Prediction ----------
if input_image is not None:

    st.subheader(f"{input_source} Result")

    st.image(
        input_image,
        caption=f"{input_source} Image",
        use_container_width=True
    )

    predicted_class, confidence = predict_image(input_image)

    st.subheader("🤖 AI Detection Result")

    st.write(
        f"**Detected Class:** {predicted_class.replace('_', ' ').title()}"
    )

    st.write(
        f"**Confidence:** {confidence:.2f}%"
    )


    # ---------- Road Safety Assistance ----------
    if predicted_class in ["closed", "yawn"]:

        st.markdown(
            f"""
            <div class="alert-box">
            ⚠️ <b>DROWSINESS DETECTED!</b><br><br>
            Detected condition: <b>{predicted_class.replace('_', ' ').title()}</b><br><br>
            🚨 Please stay alert and consider taking a break.
            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            f"""
            <div class="safe-box">
            ✅ <b>DRIVER ALERT</b><br><br>
            Detected condition: <b>{predicted_class.replace('_', ' ').title()}</b><br><br>
            👍 Driver appears to be alert.
            </div>
            """,
            unsafe_allow_html=True
        )

else:

    st.info(
        "📌 Upload a driver image or use the camera to start detection."
    )


st.write("")
st.divider()

st.caption(
    "AI Agent for Driver Drowsiness Detection and Intelligent Road Safety Assistance | EfficientNet-B0"
)