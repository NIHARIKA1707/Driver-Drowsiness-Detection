st.subheader("📷 Input")

input_method = st.radio(
    "Choose input method",
    ["📤 Upload Image", "📷 Use Camera"]
)

image = None

if input_method == "📤 Upload Image":

    uploaded_file = st.file_uploader(
        "Upload a driver image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert("RGB")

elif input_method == "📷 Use Camera":

    camera_image = st.camera_input(
        "Take a picture of the driver"
    )

    if camera_image is not None:
        image = Image.open(camera_image).convert("RGB")


# Show selected image
if image is not None:

    st.image(
        image,
        caption="Driver Image",
        use_container_width=True
    )

    st.success("✅ Image captured successfully!")

    # Prediction
    if model is not None:

        img = image.resize((224, 224))

        img_array = np.array(img) / 255.0

        img_array = np.expand_dims(img_array, axis=0)

        prediction = model.predict(img_array, verbose=0)

        predicted_index = np.argmax(prediction[0])

        class_names = [
            "Closed",
            "Open",
            "no_yawn",
            "yawn"
        ]

        predicted_class = class_names[predicted_index]

        confidence = float(prediction[0][predicted_index]) * 100

        st.subheader("🤖 Prediction")

        st.write(
            f"**Prediction:** {predicted_class}"
        )

        st.write(
            f"**Confidence:** {confidence:.2f}%"
        )

        if predicted_class in ["Closed", "yawn"]:
            st.error("🚨 DROWSY DRIVER DETECTED!")

        else:
            st.success("✅ DRIVER IS ALERT")
