import streamlit as st

st.title("Webcam")

# Captura uma imagem da câmera
img_file = st.camera_input("Capture an image")

if img_file:
    # Salva a imagem capturada
    with open("streamlit_pic.png", "wb") as f:
        f.write(img_file.getvalue())



