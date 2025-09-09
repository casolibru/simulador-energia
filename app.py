import streamlit as st
import pandas as pd
from datetime import date

# Inicializa a base fictícia de escopos
default_escopos = pd.DataFrame({
    "Escopo": [
        "Migração ACL",
        "Contratação de Energia",
        "I-RECs e Créditos de Carbono",
        "Consultoria Regulatória",
        "Orçamento de Energia"
    ],
    "Descrição": [
        "Assessoria na migração para o mercado livre de energia elétrica",
        "Processo de contratação de energia elétrica – atacado e varejo",
        "Aquisição de certificados de energia renovável (I-REC) e créditos de carbono",
        "Assessoria regulatória junto à CCEE, ANEEL, ONS e distribuidoras",
        "Previsão orçamentária por unidade consumidora com detalhamento de custos"
    ],
    "Custo (R$)": [50000, 30000, 25000, 15000, 10000],
    "Prazo (dias)": [30, 45, 40, 20, 15]
})

# Cria uma sessão de estado para manter os escopos editados
if "escopos" not in st.session_state:
    st.session_state.escopos = default_escopos.copy()

# Define as abas
aba = st.sidebar.radio("Navegação", ["📋 Preencher Proposta", "💰 Custos por Escopo"])

if aba == "📋 Preencher Proposta":
    st.title("📋 Preencher Proposta Comercial")

    # Formulário de entrada
    with st.form("form_proposta"):
        nome_empresa = st.text_input("Nome da empresa contratante")
        responsavel = st.text_input("Responsável comercial")
        validade = st.date_input("Validade da proposta", value=date.today())
        escopos_selecionados = st.multiselect(
            "Selecione os escopos desejados",
            options=st.session_state.escopos["Escopo"].tolist()
        )
        submit = st.form_submit_button("Gerar Proposta")

    # Exibe a proposta gerada
    if submit:
        st.subheader("📄 Proposta Gerada")
        st.markdown(f"**Empresa:** {nome_empresa}")
        st.markdown(f"**Responsável:** {responsavel}")
        st.markdown(f"**Validade:** {validade.strftime('%d/%m/%Y')}")
        st.markdown("---")
        for escopo in escopos_selecionados:
            dados = st.session_state.escopos[st.session_state.escopos["Escopo"] == escopo].iloc[0]
            st.markdown(f"### {dados['Escopo']}")
            st.markdown(f"- **Descrição:** {dados['Descrição']}")
            st.markdown(f"- **Custo:** R$ {dados['Custo (R$)']:.2f}")
            st.markdown(f"- **Prazo:** {dados['Prazo (dias)']} dias")
        st.markdown("---")
        st.success("Proposta simulada com sucesso! (PDF real pode ser gerado na próxima versão)")

elif aba == "💰 Custos por Escopo":
    st.title("💰 Custos por Escopo")

    # Tabela editável
    escopos_editados = st.data_editor(
        st.session_state.escopos,
        num_rows="dynamic",
        use_container_width=True
    )

    # Atualiza os escopos no estado
    st.session_state.escopos = escopos_editados

    st.info("Edite os valores acima. Eles serão usados na geração da proposta.")
