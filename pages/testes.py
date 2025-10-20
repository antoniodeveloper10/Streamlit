# import streamlit as st
#
# st.header("Utilizando a Câmera Input")
#
# # Captura uma foto da câmera
# picture = st.camera_input("Tire uma foto")
#
# # Se houver foto, exibe a imagem
# if picture:
#     st.image(picture)
#
# st.header("Color Picker")
#
# # Cria um seletor de cor
# color = st.color_picker('Escolha uma cor', '#00f900')
# st.write('A cor selecionada é:', color)
from qreader import QReader
from PIL import Image
import streamlit as st

st.title("Leitor de QR Code sem OpenCV")

uploaded = st.file_uploader("Envie uma imagem com QR Code", type=["png", "jpg", "jpeg"])
if uploaded:
    image = Image.open(uploaded)
    st.image(image)
    qreader = QReader()
    decoded = qreader.detect_and_decode(image)
    st.success(f"Conteúdo do QR Code: {decoded}")
