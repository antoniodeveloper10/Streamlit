import streamlit as st

from pages.comanda import ComandaPizzaria


class CheckoutPizzaria:
    PRECOS = ComandaPizzaria.PRECOS

    def exibir(self):
        st.title("💰 Checkout")

        numero = st.text_input("Número da comanda para checkout:")
        if not numero:
            st.info("Digite o número da comanda para visualizar o total.")
            return

        comandas = st.session_state.get("comandas", {})
        if numero not in comandas:
            st.warning("❌ Comanda não encontrada. Cadastre primeiro em 'Comanda'.")
            return

        dados = comandas[numero]
        total = 0

        st.subheader(f"🧾 Itens da Comanda {numero}")
        for item, qtd in dados.items():
            if item == "tipo":
                continue
            if qtd > 0:
                preco = self.PRECOS[item]
                subtotal = preco * qtd
                total += subtotal
                st.write(f"{item.replace('_', ' ').title()} — {qtd} × R$ {preco:.2f} = R$ {subtotal:.2f}")

        if dados["tipo"] == "rodizio":
            total += self.PRECOS["rodizio"]
            st.write(f"Rodízio — R$ {self.PRECOS['rodizio']:.2f}")

        st.markdown("---")
        st.subheader(f"💵 Total a pagar: R$ {total:.2f}")

        if st.button("✅ Finalizar Pagamento"):
            del st.session_state.comandas[numero]
            st.success(f"Pagamento da comanda {numero} realizado com sucesso!")
            st.balloons()