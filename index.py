import streamlit    as st
#
#
# pages = {
#     "Menu": [
#         st.Page("pages/home.py", title="DashBoard"),
#     ],
#     "Produção": [
#         # st.Page("pages/home.py", title="Home"),
#         st.Page("pages/Sacarias.py", title="Sacaria"),
#         st.Page("pages/comanda.py", title="Comanda"),
#         st.Page("pages/checkout.py", title="Checkout"),
#         st.Page("pages/camera.py", title="Camera"),
#     ]
# }
#
# pg = st.navigation(pages)
#
# pg.run()
#
from pages.checkout import CheckoutPizzaria
from pages.comanda import ComandaPizzaria

st.set_page_config(page_title="Sistema da Pizzaria", layout="wide")

with st.sidebar:
    st.title("🍽️ Menu")
    secao = st.radio("Selecione a seção:", ["Dashboard", "Produção", "Sacaria", "Comanda", "Checkout", "Câmera"])

# ===============================
# 🔧 Controle das telas
# ===============================
if secao == "Comanda":
    ComandaPizzaria().exibir()

elif secao == "Checkout":
    CheckoutPizzaria().exibir()

elif secao == "Dashboard":
    st.title("📊 Dashboard (em construção)")
elif secao == "Produção":
    st.title("🏭 Produção (em construção)")
elif secao == "Sacaria":
    st.title("📦 Sacaria (em construção)")
elif secao == "Câmera":
    st.title("📷 Leitor de Códigos (em construção)")
else:
    st.info("Selecione uma opção no menu lateral.")