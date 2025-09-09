import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Simulador de Economia", layout="centered")

st.title("💡 Simulador de Economia no Mercado Livre de Energia")

# Entradas do usuário
consumo = st.number_input("Consumo mensal (kWh)", min_value=0.0, value=50000.0)
tarifa_cativo = st.number_input("Tarifa mercado cativo (R$/kWh)", min_value=0.0, value=0.85)
tarifa_livre = st.number_input("Tarifa mercado livre (R$/kWh)", min_value=0.0, value=0.65)

# Botão de cálculo
if st.button("Calcular"):
    custo_cativo = consumo * tarifa_cativo
    custo_livre = consumo * tarifa_livre
    economia = custo_cativo - custo_livre
    percentual = (economia / custo_cativo) * 100 if custo_cativo > 0 else 0

    st.subheader("📊 Resultados")
    st.write(f"**Custo no mercado cativo:** R$ {custo_cativo:,.2f}")
    st.write(f"**Custo no mercado livre:** R$ {custo_livre:,.2f}")
    st.write(f"**Economia estimada:** R$ {economia:,.2f} ({percentual:.2f}%)")

    # Gráfico
    fig, ax = plt.subplots()
    ax.bar(["Cativo", "Livre"], [custo_cativo, custo_livre], color=["red", "green"])
    ax.set_ylabel("Custo (R$)")
    ax.set_title("Comparativo de Custo")
    st.pyplot(fig)
