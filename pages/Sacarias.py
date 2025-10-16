import json

import streamlit as st
from datetime import datetime, date



from Controller.controler import get_tarefa, direciona_gravacao_atualizacao
operadores_lista = [
    "Daniel",
    "Fábio",
    "Carlos",
    "Anderson",
    "Tiago",
    "João",
    "Pedro"
]

operadores_lista = [op.strip().title() for op in operadores_lista]

produto_lista = [
    "Mix Viv. Cong",
    "Mix Doce",
    "Mix Oli",
    "Mix Donafina",
    "V Plus",
    "Mix Viviana Extra Clara",
    "Sc Sublimis"
]

if "tonelada_banco" not in st.session_state:
    st.session_state.tonelada_banco = 0  #
if "qtd_batelada" not in st.session_state:
    st.session_state.qtd_batelada = 0

if "qtd_batelada_t" not in st.session_state:
    st.session_state.qtd_batelada_t = 0

if "qtd_materia_prima" not in st.session_state:
    st.session_state.qtd_materia_prima = 0

if "qtd_materia_prima_lote" not in st.session_state:
    st.session_state.qtd_materia_prima_lote = 0



if 'data_batelada' not in st.session_state:
    st.session_state.data_batelada = date.today()  # Ou uma data padrão
if "TURNO" not in st.session_state:
    st.session_state.TURNO  = "Dia"
if "MOINHO" not in st.session_state:
    st.session_state.MOINHO = "A"
st.session_state.DIA = 0
st.session_state.TAREFA_NUM  = 0
if "NOME_OPERADOR" not in st.session_state:
    st.session_state.NOME_OPERADOR = []

if "NOME_OPERADOR_ENVASE" not in st.session_state:
    st.session_state.NOME_OPERADOR_ENVASE = []

opcoes_silo = [515, 516, 517]
if "SILO" not in st.session_state or st.session_state.SILO not in opcoes_silo:
    st.session_state.SILO = opcoes_silo[0]

if "SACOS" not in st.session_state:
    st.session_state.SACOS = 0

if "PRODUTO" not in st.session_state:
    st.session_state.PRODUTO = ''

if 'LOTECP' not in st.session_state:
    st.session_state.LOTECP = ''

if 'PERCA' not in st.session_state:
    st.session_state.PERCA = 0




st.set_page_config(page_title="Formulário de Produção", layout="wide")
st.title("📋 Formulário de Produção - Viviana")

# ===============================
# 🗓️ Informações Gerais
# ===============================





with st.form("busca_data_form"):
    st.subheader("Buscar Tarefa")
    id_busca = st.number_input("ID do Registro:", min_value=1, value=1)
    buscar_btn = st.form_submit_button("🔍 Buscar")


col0 = st.columns(1)[0]
with col0:
    if buscar_btn:
        bateladas, operadores, amostras, materias = get_tarefa(id_busca)

        if  len(bateladas) == 0:
            st.warning("⚠️ Nenhum dado encontrado para os critérios de busca!")

            # Mostrar qual conjunto específico está vazio
            if not bateladas:
                st.error("• Nenhuma batelada encontrada")

            # Parar a execução ou mostrar formulário vazio
            st.stop()
        else:
            # Seu código normal continua aqui...


            data_batelada = bateladas[0]['DATA_BATELADA']
            # Armazenar no session_state para usar em outros componentes
            st.session_state.data_batelada = data_batelada

            st.session_state.qtd_batelada = bateladas[0]['QTD_BATELADAS']
            st.session_state.qtd_batelada_t = bateladas[0]['QTD_BATELADAS']





            st.session_state.tonelada_banco = bateladas[0]['TONELADAS']
            st.session_state.toneladas_1 = bateladas[0]['TONELADAS']
            #--------------------------------------

            st.session_state.qtd_materia_prima =  materias[1]['QUANTIDADE']

            st.session_state.qtd_materia_prima_lote = materias[1]['LOTE']






            #---------------------------------------------------------
            st.session_state.TURNO = bateladas[0]['TURNO']
            st.session_state.turno = bateladas[0]['TURNO']
            #------------------------------------------------------
            st.session_state.MOINHO = bateladas[0]['MOINHO']
            st.session_state.moinho = bateladas[0]['MOINHO']
            #--------------------------------------------------------
            if "DIA" not in st.session_state:
                st.session_state.DIA = ""  # ou "01/01/2025" ou qualquer valor padrão

            st.session_state.TAREFA_NUM = bateladas[0]['TAREFA_NUM']
            st.session_state.tarefa_num = bateladas[0]['TAREFA_NUM']
            #--------------------------------------------------------------
            st.session_state.NOME_OPERADOR.clear()
            st.session_state.NOME_OPERADOR_ENVASE.clear()

            for opera in operadores:
                if opera['TIPO_OPERACAO'] == "ENVASE":
                    st.session_state.NOME_OPERADOR_ENVASE.append(opera['NOME_OPERADOR'])
                else:
                    st.session_state.NOME_OPERADOR.append(opera['NOME_OPERADOR'])

            st.session_state.NOME_OPERADOR = [op.strip().title() for op in st.session_state.NOME_OPERADOR]
            st.session_state.NOME_OPERADOR_ENVASE = [op.strip().title() for op in st.session_state.NOME_OPERADOR_ENVASE]

            # if len(operadores) > 1:
            #     for opera in operadores:
            #         if opera['TIPO_OPERACAO'] == "ENVASE":
            #             st.session_state.NOME_OPERADOR_ENVASE.append(opera['NOME_OPERADOR'])
            #         else:
            #             st.session_state.NOME_OPERADOR.append(opera['NOME_OPERADOR'])
            # else:
            #     if operadores[0]['TIPO_OPERACAO'] == "ENVASE":
            #         st.session_state.NOME_OPERADOR_ENVASE = operadores[0]['NOME_OPERADOR']
            #     st.session_state.NOME_OPERADOR = operadores[0]['NOME_OPERADOR']







            #--------------------------------------------------
            st.session_state.SILO = bateladas[0]['SILO']
            st.session_state.silo = bateladas[0]['SILO']

            #----------------------------------------------
            st.session_state.SACOS = bateladas[0]['QTD_SCS']
            #------------------------------------------------------
            st.session_state.PRODUTO = bateladas[0]['PRODUTO']
            #------------------------------------------------
            st.session_state.LOTECP = bateladas[0]['LOTE_COMPLETO']
            #------------------------------------------------
            st.session_state.PERCA = bateladas[0]['PERDA_SCS']

            st.rerun()





with st.container(border=True):
    st.markdown("### ⚖️ Informações Gerais")

    # Cria 4 colunas
    col1, col2, col3, col4 = st.columns([2, 1, 1, 1])

    with col1:
        data_batelada = st.date_input(
            "Data Batelada:",
            value=st.session_state.data_batelada,
            min_value=date(1, 1, 1),
            max_value=date(9999, 12, 31)
        )

    with col2:
        turno = st.selectbox(
            "Turno",
            ["Dia", "Noite"],
            key="TURNO"
        )

    with col3:
        dia = st.text_input(
            "Dia",
            key='dia',
            value=st.session_state.DIA
        )

    with col4:
        moinho = st.selectbox(
            "Moinho",
            ["A", "B"],
            key="MOINHO"
        )

    col5, col6, col7, col8 = st.columns(4)
    with col5:
        operadores_bateladas = st.multiselect(
            "Operadores das Bateladas",
            operadores_lista,
            default=st.session_state.NOME_OPERADOR,
            key='NOME_OPERADOR',
            help="Selecione um ou mais operadores"
        )

    with col6:
        data_moagem = st.date_input("Data Moagem", datetime.today())
    with (col7):
        silo = st.selectbox("Silo", opcoes_silo, key="SILO")
        # silo = st.selectbox(
        # "Silo MAIA",
        # ["515", "516", "517"],
        # #value='SILO',
        # key='SILO',
        # help="Selecione o silo utilizado na produção"
    # )

    with col8:
        tarefa = st.text_input("Tarefa nº", value=st.session_state.TAREFA_NUM, key='tarefa_num')

# Linha de fechamento









# ===============================
# 🕐 Bateladas e Produção
# ===============================
with st.container(border=True):
    st.markdown("### 🏭 Bateladas e Produção")

    col9, col10 = st.columns(2)
    with col9:
        hora_inicial = st.time_input("Hora Inicial", key="hora_inicial_1")
        bateladas = st.number_input("Quantidade de Bateladas", min_value=0, step=1, value=st.session_state.qtd_batelada)

    with col10:
        hora_final = st.time_input("Hora Final", key="hora_final_1")
        toneladas = st.number_input("Toneladas",  min_value=0, step=1, key="toneladas_1", value=st.session_state.tonelada_banco)

    col11, col12 = st.columns(2)
    with col11:
        hora_inicial1 = st.time_input("Hora Inicial", key="hora_inicial_2")
        bateladas1 = st.number_input("Quantidade Segunda Bateladas", min_value=0, step=1, value=st.session_state.qtd_batelada_t)
    with col12:
        hora_final1 = st.time_input("Hora Final", key="hora_final_2")
        toneladas1 = st.number_input("Toneladas", min_value=0, step= 1, key="toneladas_2")





# ===============================
# 📦 Envase
# ===============================
with st.container(border=True):
    st.markdown("### 📦 Envase")
    col13, col14 = st.columns(2)
    with col13:
        data_envase = st.date_input("Data Envase", datetime.today())
    with col14:
        operadores_envases = st.multiselect(
            "Operadores do Envase",
            operadores_lista,
            default=st.session_state.NOME_OPERADOR_ENVASE,
            key='NOME_OPERADOR_ENVASE',
            help="Selecione um ou mais operadores"
        )

    qtd_scs = st.number_input("Quantidade (scs)", min_value=0, step=1,key='SACOS',value=st.session_state.SACOS)
    perda_scs = st.number_input("Perda (scs)", min_value=0, step=1, key='PERCA', value=st.session_state.PERCA)
    lote_completo = st.text_input("Lote Completo",key='LOTECP',value=st.session_state.LOTECP)
#lote_completo = st.text_input("Lote Completo")
#ultimo_sc = st.text_input("Último sc. L")

# ===============================
# 📊 Amostras
# ===============================

    col15, col16, col17, col18 = st.columns(4)
    with col15:
        amostra1 = st.text_input("1ª Padaria")
    with col16:
        amostra2 = st.text_input("2ª Padaria")
    with col17:
        amostra3 = st.text_input("3ª Padaria")
    with col18:
        amostra4 = st.text_input("4ª Padaria")

# ===============================
# 🏭 Matéria-prima e embalagens
# ===============================

    col19 = st.columns(1)[0]
    with col19:
        produtos = st.selectbox("Produto", produto_lista, key="PRODUTO")



st.subheader("Gastos de Matéria-Prima / Embalagens")

materia_primas = [
    "Sal",
    "Açúcar Ref.",
    # "Megapan 10144",
    # "Powerzyme 10869",
]

dados_materia_prima = {}
with st.container(border=True):
    st.markdown("### 🔬 Produção de Farinhas")
    for mp in materia_primas:
        colA, colB = st.columns([2, 1])
        with colA:
            quantidade = st.text_input(f"Quantidade - {mp}",value= st.session_state.qtd_materia_prima)
        with colB:
            lote = st.text_input(f"Lote - {mp}",value=st.session_state.qtd_materia_prima_lote)
        dados_materia_prima[mp] = {"Quantidade": quantidade, "Lote": lote}

with st.container(border=True):

    # ===============================
    # 🟢 Botões lado a lado e coloridos
    # ===============================
    col1, col2, col3 = st.columns([1, 1, 1])  # colunas proporcionais (centraliza os botões)

    with col1:
        st.empty()  # espaço à esquerda

    with col2:
        salvar = st.button("💾 Salvar / Enviar", use_container_width=True)
        if salvar:
            dados = {
                "Data Batelada": str(data_batelada),
                "Turno": turno,
                "Dia": dia,
                "Moinho": moinho,
                "Operador Bateladas": operadores_bateladas,
                "Data Moagem": str(data_moagem),
                "Silo": silo,
                "Tarefa nº": tarefa,
                "Quantidade Bateladas": bateladas,
                "Toneladas": toneladas,
                "Hora Inicial": str(hora_inicial),
                "Hora Final": str(hora_final),
                "Quantidade Bateladas1": bateladas,
                "Toneladas1": toneladas,
                "Hora Inicial1": str(hora_inicial),
                "Hora Final1": str(hora_final),
                "Data Envase": str(data_envase),
                "Operador Envase": operadores_envases,
                "Qtd scs": qtd_scs,
                "Perda scs": perda_scs,
                "Lote Completo": lote_completo,
                "Materias primas": dados_materia_prima,
                "Produto": produtos
            }
            print('dados carregados' + dados)

            json_string = json.dumps(dados)
            if direciona_gravacao_atualizacao(dados["Tarefa nº"], json_string):
                st.success("✅ Formulário enviado com sucesso!")
            else:
                st.error("🚨 Dados não salvos!")

    with col3:
        atualizar = st.button("🔁 Atualizar", use_container_width=True)
        if atualizar:
            dados = {
                "Data Batelada": str(data_batelada),
                "Turno": turno,
                "Dia": dia,
                "Moinho": moinho,
                "Operador Bateladas": operadores_bateladas,
                "Data Moagem": str(data_moagem),
                "Silo": silo,
                "Tarefa nº": tarefa,
                "Quantidade Bateladas": bateladas,
                "Toneladas": toneladas,
                "Hora Inicial": str(hora_inicial),
                "Hora Final": str(hora_final),
                "Quantidade Bateladas1": bateladas,
                "Toneladas1": toneladas,
                "Hora Inicial1": str(hora_inicial),
                "Hora Final1": str(hora_final),
                "Data Envase": str(data_envase),
                "Operador Envase": operadores_envases,
                "Qtd scs": qtd_scs,
                "Perda scs": perda_scs,
                "Lote Completo": lote_completo,
                "Materias primas": dados_materia_prima,
                "Produto": produtos
            }

            json_string = json.dumps(dados)
            if direciona_gravacao_atualizacao(dados["Tarefa nº"], json_string):
                st.success("✅ Dados atualizados com sucesso!")
            else:
                st.error("🚨 Atualização falhou!")

    # ===============================
    # 🎨 Estilo CSS para colorir botões
    # ===============================
    st.markdown(
        """
        <style>
        div[data-testid="column"]:has(button) button:first-child {
            background-color: #2ecc71 !important; /* verde */
            color: white !important;
            font-weight: bold;
            border: none;
        }
        div[data-testid="column"]:has(button) button:last-child {
            background-color: #3498db !important; /* azul */
            color: white !important;
            font-weight: bold;
            border: none;
        }
        </style>
        """,
        unsafe_allow_html=True
    )



        # st.json(dados)

        #save_tarefa(json_string)
