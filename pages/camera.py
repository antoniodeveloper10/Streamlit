import streamlit as st
from PIL import Image
from pyzbar.pyzbar import decode

st.title("Leitor de Código de Barras")

# Captura a foto usando a câmera
foto = st.camera_input("Aponte a câmera para o código de barras")

if foto:
    # Mostra a imagem capturada
    st.image(foto)

    # Converte a imagem para PIL
    imagem = Image.open(foto)

    # Decodifica códigos de barra
    codigos = decode(imagem)

    if codigos:
        for codigo in codigos:
            st.success(f"Código lido: {codigo.data.decode('utf-8')}")
    else:
        st.warning("Nenhum código de barras detectado.")
