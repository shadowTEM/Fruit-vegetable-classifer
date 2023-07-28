import streamlit as st
from PIL import Image
from GUIFunction import GFunction

uploaded_file = st.file_uploader("Hello please enter your picture here jpg formate only", type=[ "jpg"])
if uploaded_file is not None:
    # Use PIL to open and display the image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    button_clicked = st.button("Predict")
    if button_clicked:
        save_path = "G:\\Fruit and veg\\Fruit_recognition\\image.jpg"  # Replace with the desired save path
        image.save(save_path)
        image_path =save_path
        st.write(GFunction(image_path))



