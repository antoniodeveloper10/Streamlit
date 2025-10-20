import streamlit as st

# ===============================
# 🍕 Classe 1: Alimentar Comanda
# ===============================

PRECOS = {
    "rodizio": 59.90,
    "refrigerante": 6.00,
    "cerveja": 9.00,
    "vinho": 80.00,
    "batata": 15.00,
    "pizza_individual": 38.00,
    "pizza_grande": 65.00,
    "lasanha": 42.00,
    "macarrao": 35.00,
    "sobremesa": 18.00,
}


if "comandas" not in st.session_state:
    st.session_state.comandas = {}

    #def exibir(self):
st.title("🍕 Abrir Comanda")

numero = st.text_input("Número da comanda:")
if not numero:
    st.info("Digite o número da comanda para começar.")


tipo = st.radio("Tipo de atendimento:", ["Rodízio", "À la carte"])

st.subheader("🥤 Bebidas e acompanhamentos")
refrigerantes = st.number_input("Refrigerantes (unid.)", 0, 50, 0)
cervejas = st.number_input("Cervejas (unid.)", 0, 50, 0)
vinhos = st.number_input("Garrafas de vinho", 0, 10, 0)
batata = st.number_input("Porções de batata frita", 0, 20, 0)

pizza_individual = pizza_grande = lasanha = macarrao = sobremesa = 0

if tipo == "À la carte":
    st.subheader("🍝 Pratos e Pizzas")
    pizza_individual = st.number_input("Pizza individual", 0, 10, 0)
    pizza_grande = st.number_input("Pizza grande", 0, 10, 0)
    lasanha = st.number_input("Lasanha", 0, 10, 0)
    macarrao = st.number_input("Macarrão", 0, 10, 0)
    sobremesa = st.number_input("Sobremesas", 0, 10, 0)

if st.button("💾 Salvar Comanda"):
    st.session_state.comandas[numero] = {
        "tipo": tipo.lower().replace(" ", ""),
        "refrigerante": refrigerantes,
        "cerveja": cervejas,
        "vinho": vinhos,
        "batata": batata,
        "pizza_individual": pizza_individual,
        "pizza_grande": pizza_grande,
        "lasanha": lasanha,
        "macarrao": macarrao,
        "sobremesa": sobremesa,
    }
    st.success(f"✅ Comanda {numero} salva com sucesso!")