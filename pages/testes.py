# app.py
import streamlit as st
from PIL import Image
import tempfile
from pyzxing import BarCodeReader

st.title("📷 Leitor de Código de Barras 1D (Cloud-friendly)")

# Captura imagem
image_file = st.camera_input("Aponte a câmera para o código de barras")

if image_file is not None:
    # Salva a imagem temporariamente
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp_file:
        tmp_file.write(image_file.read())
        tmp_filename = tmp_file.name

    # Inicializa leitor
    reader = BarCodeReader()
    result = reader.decode(tmp_filename)

    if result:
        st.success("Código de barras detectado!")
        for r in result:
            st.write(f"Tipo: {r['type']}")
            st.write(f"Dados: {r['raw']}")
    else:
        st.warning("Nenhum código de barras detectado.")
