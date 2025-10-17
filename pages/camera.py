import streamlit as st
import cv2
from qreader import QReader
from PIL import Image
import numpy as np

st.title("📷 Leitor de QR Code com Streamlit")

# Captura da câmera
img_file = st.camera_input("Aponte para um QR Code")

if img_file:
    # Converte a imagem
    img = Image.open(img_file)
    frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

    # Inicializa o leitor de QR
    qreader = QReader()
    decoded_text = qreader.detect_and_decode(image=frame)

    if decoded_text:
        st.success(f"✅ QR Code detectado: {decoded_text}")
    else:
        st.warning("Nenhum QR Code encontrado.")
