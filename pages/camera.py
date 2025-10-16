import streamlit as st
from PIL import Image
from pyzbar.pyzbar import decode

st.title("Leitor de Código de Barras no Celular")

# Abre a câmera do celular
foto = st.camera_input("Aponte a câmera para o código de barras ou QR code")

if foto:
    st.image(foto)  # mostra a foto na tela

    # Converte para PIL
    imagem = Image.open(foto)

    # Decodifica códigos de barra
    codigos = decode(imagem)

    if codigos:
        for codigo in codigos:
            st.success(f"Código lido: {codigo.data.decode('utf-8')}")
    else:
        st.warning("Nenhum código de barras detectado.")


