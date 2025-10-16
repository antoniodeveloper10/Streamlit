import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.title("Leitor de QR Code pelo celular")

# Botão para abrir a câmera
if st.button("Abrir câmera"):
    img_file = st.camera_input("Aponte a câmera para o QR Code")

    if img_file:
        # Converte para imagem PIL
        img = Image.open(img_file)
        st.image(img, caption="Imagem capturada", use_column_width=True)

        # Converte para OpenCV
        img_cv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

        # Detecta QR Code
        detector = cv2.QRCodeDetector()
        data, bbox, _ = detector.detectAndDecode(img_cv)

        if data:
            st.success(f"QR Code detectado: {data}")
        else:
            st.warning("Nenhum QR Code detectado.")
