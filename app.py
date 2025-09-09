import streamlit as st

# Configuração da página
st.set_page_config(page_title="FLL Robot Tester", layout="wide")

# Cabeçalho
st.markdown(
    """
    <div style="background-color:#2563eb;padding:20px;border-radius:10px;text-align:center;">
        <h1 style="color:white; margin:0;">🤖 FLL Robot Tester</h1>
        <p style="color:white; margin:0;">Sistema de análise e acompanhamento de testes para robôs da First Lego League</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("## Escolha o Tipo de Teste")
st.write("Selecione um dos tipos de teste abaixo para visualizar os resultados e acompanhar as melhorias implementadas no robô.")

# Layout com 3 colunas para os cards
col1, col2, col3 = st.columns(3)

with col1:
    st.image("https://i.ibb.co/k1VDz7R/robo1.png", use_column_width=True)
    st.markdown("### Teste de Giro")
    st.write("Análise de precisão e controle de rotação do robô")
    if st.button("Abrir Teste de Giro"):
        st.success("Abrindo página de Teste de Giro...")

with col2:
    st.image("https://i.ibb.co/m8z9jLq/robo2.png", use_column_width=True)
    st.markdown("### Teste de Reta")
    st.write("Avaliação de movimentação linear e estabilidade")
    if st.button("Abrir Teste de Reta"):
        st.success("Abrindo página de Teste de Reta...")

with col3:
    st.image("https://i.ibb.co/3zVjtdg/robo3.png", use_column_width=True)
    st.markdown("### Teste de Pontuação")
    st.write("Verificação de performance em missões competitivas")
    if st.button("Abrir Teste de Pontuação"):
        st.success("Abrindo página de Teste de Pontuação...")
