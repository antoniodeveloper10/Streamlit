import streamlit as st

st.set_page_config(page_title="Leitor de Barras em Runtime", layout="centered")

st.title("📦 Leitor de Código de Barras com Numeração")

# Inicializa o estado da sessão
if "dados" not in st.session_state:
    st.session_state.dados = {}
if "ultimo_codigo" not in st.session_state:
    st.session_state.ultimo_codigo = ""

# Campo da numeração
num = st.number_input("🔢 Escolha a numeração:", min_value=1, step=1)

# Criamos um formulário para processar o código de barras
with st.form("form_codigo", clear_on_submit=True):
    codigo = st.text_input("📸 Leitor de código de barras (pressione Enter após leitura):", key="codigo_input")
    submitted = st.form_submit_button("Adicionar")

if submitted and codigo:
    # Evita leitura duplicada
    if codigo != st.session_state.ultimo_codigo:
        st.session_state.ultimo_codigo = codigo
        st.session_state.dados.setdefault(num, []).append(codigo)

# Exibe a lista em tempo real
st.subheader(f"📋 Lista de códigos — Numeração {num}")

if num in st.session_state.dados and st.session_state.dados[num]:
    for i, c in enumerate(st.session_state.dados[num], 1):
        st.write(f"{i}. {c}")
else:
    st.info("Nenhum código lido ainda para esta numeração.")

# Botão para limpar dados da numeração
if st.button("🧹 Limpar numeração atual"):
    if num in st.session_state.dados:
        del st.session_state.dados[num]
        st.session_state.ultimo_codigo = ""
