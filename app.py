import streamlit as st

# Configuração da página
st.set_page_config(page_title="Painel de Testes The Crew", layout="wide")

# ====== CSS GLOBAL ======
st.markdown(
    """
    <style>
    body {
        background-color: #f4f6f9;
        font-family: "Segoe UI", sans-serif;
    }
    /* Cabeçalho */
    .header {
        background: linear-gradient(90deg, #2563eb, #1e3a8a);
        padding: 20px 40px;
        border-radius: 12px;
        color: white;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
    .header h1 {
        margin: 0;
        font-size: 28px;
    }
    .header p {
        margin: 0;
        font-size: 14px;
        opacity: 0.9;
    }
    /* Cards */
    .card {
        background-color: white;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0 2px 6px rgba(0,0,0,0.1);
        transition: transform 0.2s, box-shadow 0.2s;
    }
    .card:hover {
        transform: translateY(-3px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }
    .card-title {
        font-size: 18px;
        font-weight: bold;
        margin-top: 10px;
    }
    .card-desc {
        font-size: 13px;
        color: #6b7280;
        margin-bottom: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ====== CABEÇALHO ======
st.markdown(
    """
    <div class="header">
        <div>
            <h1>Painel de Testes The Crew</h1>
            <p>Sistema de análise e acompanhamento de testes – Temporada Unearthed</p>
        </div>
        <div>
            <a href='#'>
                <button style="
                    background-color:white;
                    color:#2563eb;
                    padding:8px 16px;
                    border:none;
                    border-radius:8px;
                    font-weight:bold;
                    cursor:pointer;
                ">📊 Relatório Geral</button>
            </a>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# ====== KPIs ======
st.write(" ")
kpi1, kpi2, kpi3 = st.columns(3)
kpi1.metric("📊 Tipos de Teste", 6)
kpi2.metric("✅ Testes Concluídos", 268)
kpi3.metric("⚙️ Melhorias Aplicadas", 34)

st.write("---")

# ====== GRID DE TESTES ======
st.subheader("Testes Disponíveis")

def criar_card(imagem, titulo, descricao, link):
    st.markdown(
        f"""
        <a href="{link}" style="text-decoration:none; color:inherit;">
        <div class="card">
            <img src="{imagem}" width="200">
            <div class="card-title">{titulo}</div>
            <div class="card-desc">{descricao}</div>
        </div></a>
        """,
        unsafe_allow_html=True
    )

testes = [
    {
        "imagem": "https://i.ibb.co/k1VDz7R/robo1.png",
        "titulo": "Testes de Giro",
        "descricao": "Análise de precisão e controle de rotação do robô",
        "link": "teste_giro",
    },
    {
        "imagem": "https://i.ibb.co/m8z9jLq/robo2.png",
        "titulo": "Testes de Reta",
        "descricao": "Avaliação de movimentação linear e estabilidade",
        "link": "teste_giro",
    },
    {
        "imagem": "https://i.ibb.co/m8z9jLq/robo2.png",
        "titulo": "Testes de Saídas",
        "descricao": "Avaliação de movimentação linear e estabilidade",
        "link": "teste_giro",
    },
    {
        "imagem": "https://i.ibb.co/m8z9jLq/robo2.png",
        "titulo": "Testes de Missões",
        "descricao": "Avaliação de movimentação linear e estabilidade",
        "link": "teste_missoes",
    },
    {
        "imagem": "https://i.ibb.co/m8z9jLq/robo2.png",
        "titulo": "Testes de Rodas",
        "descricao": "Avaliação de movimentação linear e estabilidade",
        "link": "teste_giro",
    },
    {
        "imagem": "https://i.ibb.co/m8z9jLq/robo2.png",
        "titulo": "Testes de Rounds",
        "descricao": "Avaliação de movimentação linear e estabilidade",
        "link": "teste_rounds",
    }
]

cols = st.columns(5)
for i, teste in enumerate(testes):
    with cols[i % 5]:
        criar_card(
            teste["imagem"],
            teste["titulo"],
            teste["descricao"],
            teste["link"],
        )
