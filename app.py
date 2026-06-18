import streamlit as st
st.write("APP BERHASIL DIMUAT")
from PIL import Image

from utils.predict import predict_style



# PAGE CONFIG

st.set_page_config(
    page_title="Fashion Style Detector",
    page_icon="👗",
    layout="centered"
)

# TITLE
st.title("👗 Fashion Style Detector")
st.write(
    "Upload outfit kamu dan temukan style fashion-mu!"
)

# UPLOAD IMAGE
uploaded_file = st.file_uploader(
    "Upload gambar outfit",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    # SHOW IMAGE
    st.image(
        image,
        caption="Uploaded Outfit",
        use_container_width=True
    )

    # BUTTON
    if st.button("Analyze Fashion Item"):

        with st.spinner("Analyzing item..."):

            style, confidence = predict_style(image)

        # RESULT
        st.success(f"Style Detected: {style}")

        st.write(
            f"Confidence: {confidence:.2%}"
        )

        