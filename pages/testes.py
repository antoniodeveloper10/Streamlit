# app.py
import streamlit as st

class ComandaPizzaria:
    def __init__(self):
        self.tipo_servico = None
        self.refrigerantes = 0
        self.vinhos = 0
        self.cervejas = 0
        self.batatas = 0

        # Tabela de preços
        self.precos = {
            "rodizio": 59.90,
            "pizza_individual": 42.00,
            "refrigerante": 6.00,
            "vinho": 75.00,
            "cerveja": 10.00,
            "batata": 18.00
        }

    def escolher_servico(self):
        st.header("🍕 Escolha o tipo de serviço")
        self.tipo_servico = st.radio(
            "Selecione uma opção:",
            ("Rodízio", "À la carte")
        )

    def selecionar_itens(self):
        st.header("🥤 Bebidas e acompanhamentos")
        self.refrigerantes = st.number_input("Refrigerantes", min_value=0, step=1)
        self.vinhos = st.number_input("Garrafas de vinho", min_value=0, step=1)
        self.cervejas = st.number_input("Cervejas", min_value=0, step=1)
        self.batatas = st.number_input("Porções de batata frita", min_value=0, step=1)

    def calcular_total(self):
        total = 0

        # Tipo de serviço
        if self.tipo_servico == "Rodízio":
            total += self.precos["rodizio"]
        else:
            total += self.precos["pizza_individual"]

        # Bebidas e acompanhamentos
        total += self.refrigerantes * self.precos["refrigerante"]
        total += self.vinhos * self.precos["vinho"]
        total += self.cervejas * self.precos["cerveja"]
        total += self.batatas * self.precos["batata"]

        return total

    def mostrar_resumo(self):
        st.header("📋 Resumo da comanda")
        total = self.calcular_total()

        st.write(f"**Tipo de serviço:** {self.tipo_servico}")
        st.write(f"**Refrigerantes:** {self.refrigerantes}")
        st.write(f"**Vinhos:** {self.vinhos}")
        st.write(f"**Cervejas:** {self.cervejas}")
        st.write(f"**Batatas fritas:** {self.batatas}")
        st.write("---")
        st.success(f"💰 **Total a pagar:** R$ {total:.2f}")

# ==============================
# Interface principal Streamlit
# ==============================

st.title("🍕 Comanda Digital - Pizzaria da Viviana")

comanda = ComandaPizzaria()

comanda.escolher_servico()
comanda.selecionar_itens()

if st.button("Finalizar Pedido"):
    comanda.mostrar_resumo()
