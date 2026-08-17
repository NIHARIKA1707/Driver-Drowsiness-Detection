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

st.subheader("📷 Upload Driver Image")

uploaded_file = st.file_uploader(
    "Choose an image of the driver",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.subheader("Uploaded Driver Image")

    st.image(
        image,
        caption="Uploaded Driver Image",
        use_container_width=True
    )

    st.write("")

    st.subheader("Detection Result")

    st.write("**Detected Class:** Yawn")
    st.write("**Confidence:** 88.58%")

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
        📌 Please upload a driver image to view the detection result.
        </div>
        """,
        unsafe_allow_html=True
    )

st.write("")
st.divider()

st.caption(
    "Driver Drowsiness Detection | B.Tech Project | Frontend Demonstration"
)