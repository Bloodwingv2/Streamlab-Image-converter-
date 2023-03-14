import streamlit as st
import requests

img = st.file_uploader("Upload Image : ", type=["jpg", "png", "jpeg"])

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Convert to Grayscale"):
        if img is not None:
            response = requests.post(
                url="http://127.0.0.1:5000/grayscale",
                files={'file': img.getvalue()}
            )

            st.image(response.content)

with col2:
    if st.button('Edge Detection'):
        if img is not None:
            response = requests.post(
                url="http://127.0.0.1:5000/canny",
                files={'file': img.getvalue()}
            )

            st.image(response.content)

with col3:
    if st.button('Contours Detector'):
        if img is not None:
            response = requests.post(
                url="http://127.0.0.1:5000/contours",
                files={'file': img.getvalue()}
            )

            st.image(response.content)