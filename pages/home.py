import streamlit as st
import time

# --- Simula uma função que busca valor no banco ---
def buscar_toneladas_no_banco():
    # aqui você colocaria sua consulta SQL real
    time.sleep(1)  # simula tempo de busca
    return 42  # exemplo: valor vindo do banco

# --- Inicializa session_state ---
if "testar" not in st.session_state:
    st.session_state.testar = 10  # valor inicial

st.title("Exemplo: Buscar valor no banco e atualizar campo")

st.write("Toneladas atuais:", st.session_state.testar)

# --- Botão que busca no banco e atualiza o valor ---
if st.button("🔍 Buscar valor no banco"):
    novo_valor = buscar_toneladas_no_banco()
    st.session_state.testar = novo_valor
    st.session_state.toneladas_1 = novo_valor  # atualiza o componente diretamente
    st.success(f"Valor buscado: {novo_valor}")
    st.rerun()  # recarrega a interface com o novo valor

# --- Campo de entrada ---
toneladas = st.number_input(
    "Toneladas",
    min_value=0,
    step=1,
    key="toneladas_1",
    value=st.session_state.testar
)

# --- Atualiza o estado se o usuário alterar o valor manualmente ---
st.session_state.testar = toneladas

st.write("Valor atualizado:", st.session_state.testar)