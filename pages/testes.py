import streamlit as st
import mysql.connector
from datetime import date

from Controller.controler import get_tarefa, save_tarefa



# Interface
st.title("📊 Sistema de Data Batelada")

json_text = """ {
  "Data Batelada": "2025-10-09",
  "Turno": "Dia",
  "Dia": "0",
  "Moinho": "A",
  "Operador Bateladas": [
    "Carlos",
    "João"
  ],
  "Data Moagem": "2025-10-10",
  "Silo": 515,
  "Tarefa nº": "12345",
  "Quantidade Bateladas": 65,
  "Toneladas": 800,
  "Hora Inicial": "11:12:00",
  "Hora Final": "11:12:00",
  "Quantidade Bateladas1": 65,
  "Toneladas1": 800,
  "Hora Inicial1": "11:12:00",
  "Hora Final1": "11:12:00",
  "Data Envase": "2025-10-10",
  "Operador Envase": [
    "Carlos",
    "Tiago"
  ],
  "Qtd scs": 20,
  "Perda scs": 2,
  "Lote Completo": "ddferrer2468449rgrere468",
  "Matérias-primas": {
    "Sal": {
      "Quantidade": "10.00",
      "Lote": null
    },
    "Açúcar Ref.": {
      "Quantidade": "10.00",
      "Lote": null
    }
  },
  "Produto": "Mix Viv. Cong"
}"""
save_tarefa(json_text)
# Formulário de busca
with st.form("busca_data_form"):
    st.subheader("Buscar Data do Banco")
    id_busca = st.number_input("ID do Registro:", min_value=1, value=1)
    buscar_btn = st.form_submit_button("🔍 Buscar Data Batelada")

if buscar_btn:
    with st.spinner("Buscando data no banco..."):
        bateladas, operadores, amostras, materias = get_tarefa(id_busca)

    if bateladas:
        data_batelada = bateladas[0]['DATA_BATELADA']
        # Armazenar no session_state para usar em outros componentes
        st.session_state.data_batelada = data_batelada

        st.success(f"✅ Data carregada: {data_batelada}")

        # Componente principal com a data do banco
        col1, col2= st.columns([2, 1])

        with col1:
            data_editavel = st.date_input(
                "Data Batelada:",
                value=st.session_state.data_batelada,
                min_value=date(1, 1, 1),
                max_value=date(9999, 12, 31),
                help="Data carregada do banco de dados"
            )

            # Data formatada em português
            data_formatada = data_editavel.strftime('%d/%m/%Y')

            # Exibir de forma destacada
            st.markdown(f"""
                       <div style='
                           background: #f8f9fa;
                           padding: 15px;
                           border-radius: 8px;
                           border-left: 4px solid #ff4b4b;
                           margin: 10px 0;
                       '>
                           <strong>Data Formatada:</strong><br>
                           <span style='font-size: 1.2em; color: #262730;'>{data_formatada}</span>
                       </div>
                       """, unsafe_allow_html=True)
            # data_editavel = st.date_input(
            #     "Data Batelada:",
            #     value=st.session_state.data_batelada,
            #     min_value=date(1, 1, 1),
            #     max_value=date(9999, 12, 31),
            #     help="Data carregada do banco de dados"
            # )

        with col2:
            st.metric("Dia", data_batelada.day)
            st.metric("Mês", data_batelada.month)
            st.metric("Ano", data_batelada.year)




        # Botão para atualizar no banco (se necessário)
        if st.button("💾 Salvar Alterações"):
            # Aqui você pode adicionar a lógica para atualizar no MySQL
            st.success(f"Data {data_editavel} salva com sucesso!")

    else:
        st.error("❌ Nenhuma data batelada encontrada no banco!")

# Mostrar estado inicial se não houve busca
if not st.session_state.get('data_batelada') and not buscar_btn:
    st.info("👆 Clique em 'Buscar Data Batelada' para carregar os dados do banco")