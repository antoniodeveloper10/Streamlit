# import streamlit as st
# import cv2
# import tempfile
# from pyzxing import BarCodeReader
# from PIL import Image
#
# st.title("Leitor de QR Code - Streamlit Cloud")
#
# uploaded_file = st.file_uploader("Envie uma imagem com QR Code", type=["jpg", "png", "jpeg"])
#
# if uploaded_file:
#     # Salva a imagem temporariamente
#     with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
#         temp_file.write(uploaded_file.read())
#         temp_path = temp_file.name
#
#     # Mostra a imagem
#     image = Image.open(temp_path)
#     st.image(image, caption="Imagem enviada", use_container_width=True)
#
#     # Decodifica o QR
#     reader = BarCodeReader()
#     result = reader.decode(temp_path)
#
#     if result:
#         st.success("✅ QR Code detectado:")
#         st.json(result)
#     else:
#         st.error("❌ Nenhum QR Code encontrado.")

import streamlit as st
import cv2
import numpy as np
from PIL import Image
import tempfile

st.title("Leitor de QR Code via Webcam - Streamlit Cloud")

# Captura da câmera
picture = st.camera_input("Tire uma foto do QR Code")

if picture:
    # Salva temporariamente a imagem
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
        temp_file.write(picture.read())
        temp_path = temp_file.name

    # Mostra a imagem
    image = Image.open(temp_path)
    st.image(image, caption="Imagem capturada", use_container_width=True)

    # Converte para OpenCV
    image_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    # Detecta e decodifica o QR Code
    detector = cv2.QRCodeDetector()
    data, bbox, _ = detector.detectAndDecode(image_cv)

    if bbox is not None and data:
        st.success(f"✅ QR Code detectado: {data}")
    else:
        st.error("❌ Nenhum QR Code encontrado.")

