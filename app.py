import streamlit as st

# Configuração da página
st.set_page_config(page_title="Painel de Testes The Crew", layout="wide")

# Cabeçalho
st.markdown(
    """
    <div style="background-color:#2563eb;padding:20px;border-radius:10px;text-align:center;">
        <h1 style="color:white; margin:0;">Painel de Testes The Crew</h1>
        <p style="color:white; margin:0;">Sistema de análise e acompanhamento de testes temporada Unearthed</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("## Escolha o Tipo de Teste")
st.write("Clique em um dos cards abaixo para visualizar os resultados e acompanhar as melhorias implementadas no robô.")

# Layout com 3 colunas
col1, col2, col3, col4, col5 = st.columns(5)

# Card 1
with col1:
    st.image("https://i.ibb.co/k1VDz7R/robo1.png", use_container_width=True)
    st.markdown("### Teste de Giro")
    st.write("Análise de precisão e controle de rotação do robô")
    st.page_link("pages/teste_giro.py", label="Abrir Teste de Giro", icon="➡️")

# Card 2
with col2:
    st.image("https://i.ibb.co/m8z9jLq/robo2.png", use_container_width=True)
    st.markdown("### Teste de Reta")
    st.write("Avaliação de movimentação linear e estabilidade")
    st.page_link("pages/teste_reta.py", label="Abrir Teste de Reta", icon="➡️")

# Card 2
with col3:
    st.image("https://i.ibb.co/m8z9jLq/robo2.png", use_container_width=True)
    st.markdown("### Teste de Reta")
    st.write("Avaliação de movimentação linear e estabilidade")
    st.page_link("pages/teste_reta.py", label="Abrir Teste de Reta", icon="➡️")

# Card 2
with col4:
    st.image("https://i.ibb.co/m8z9jLq/robo2.png", use_container_width=True)
    st.markdown("### Teste de Reta")
    st.write("Avaliação de movimentação linear e estabilidade")
    st.page_link("pages/teste_reta.py", label="Abrir Teste de Reta", icon="➡️")

# Card 2
with col5:
    st.image("https://i.ibb.co/m8z9jLq/robo2.png", use_container_width=True)
    st.markdown("### Teste de Reta")
    st.write("Avaliação de movimentação linear e estabilidade")
    st.page_link("pages/teste_reta.py", label="Abrir Teste de Reta", icon="➡️")

