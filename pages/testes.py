import streamlit as st

st.header("Utilizando a Câmera Input")

# Captura uma foto da câmera
picture = st.camera_input("Tire uma foto")

# Se houver foto, exibe a imagem
if picture:
    st.image(picture)

st.header("Color Picker")

# Cria um seletor de cor
color = st.color_picker('Escolha uma cor', '#00f900')
st.write('A cor selecionada é:', color)
