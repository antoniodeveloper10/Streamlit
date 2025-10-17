from PIL import Image
from pyzbar.pyzbar import decode
import streamlit as st

st.title("📱 Leitor de QR Code")

picture = st.camera_input("Aponte para o QR Code e tire uma foto")

if picture:
    img = Image.open(picture)
    decoded = decode(img)
    if decoded:
        st.success("✅ QR Code detectado!")
        for obj in decoded:
            st.write("**Conteúdo:**", obj.data.decode("utf-8"))
    else:
        st.warning("⚠️ Nenhum QR Code encontrado.")
