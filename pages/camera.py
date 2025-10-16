import streamlit as st
from PIL import Image
from pyzbar.pyzbar import decode

st.title("Leitor de QR Code para celular / Streamlit Cloud")

# Botão para abrir a câmera
if st.button("Abrir câmera"):
    img_file = st.camera_input("Aponte a câmera para o QR Code")

    if img_file:
        # Converte para imagem PIL
        img = Image.open(img_file)
        st.image(img, caption="Imagem capturada", use_column_width=True)

        # Decodifica o QR code
        decoded_objects = decode(img)
        if decoded_objects:
            for obj in decoded_objects:
                st.success(f"QR Code detectado: {obj.data.decode('utf-8')}")
        else:
            st.warning("Nenhum QR Code detectado.")
