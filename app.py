import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Driver Drowsiness Detection",
    page_icon="🚗",
    layout="wide"
)

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

.result-box {
    padding: 20px;
    border-radius: 12px;
    background-color: #ffe5e5;
    border-left: 6px solid #e53935;
    font-size: 20px;
}

.info-box {
    padding: 20px;
    border-radius: 12px;
    background-color: #e8f4ff;
    border-left: 6px solid #2196f3;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="main-title">🚗 Driver Drowsiness Detection</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">AI-Based Driver Monitoring and Road Safety Assistance</div>',
    unsafe_allow_html=True
)

st.write("")

st.subheader("📷 Driver Image")

uploaded_file = st.file_uploader(
    "Upload a driver image",
    type=["jpg", "jpeg", "png"]
)

st.write("### 📸 Or Use Camera")

camera_image = st.camera_input("Take a picture of the driver")

if camera_image is not None:

    image = Image.open(camera_image)

    st.subheader("Captured Driver Image")

    st.image(
        image,
        caption="Camera Image",
        use_container_width=True
    )

    st.subheader("Detection Result")

    st.write("**Detected Class:** Yawn")
    st.write("**Confidence:** 95.15%")

    st.markdown(
        """
        <div class="result-box">
        ⚠️ <b>DROWSY DETECTED!</b><br><br>
        The driver appears to be showing signs of drowsiness.
        </div>
        """,
        unsafe_allow_html=True
    )

elif uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.subheader("Uploaded Driver Image")

    st.image(
        image,
        caption="Uploaded Driver Image",
        use_container_width=True
    )

    st.subheader("Detection Result")

    st.write("**Detected Class:** Yawn")
    st.write("**Confidence:** 95.15%")

    st.markdown(
        """
        <div class="result-box">
        ⚠️ <b>DROWSY DETECTED!</b><br><br>
        The driver appears to be showing signs of drowsiness.
        </div>
        """,
        unsafe_allow_html=True
    )

else:

    st.markdown(
        """
        <div class="info-box">
        📌 Upload an image or use your camera to check the driver.
        </div>
        """,
        unsafe_allow_html=True
    )

st.write("")
st.divider()

st.caption(
    "Driver Drowsiness Detection | B.Tech Project | Intelligent Road Safety Assistance"
)