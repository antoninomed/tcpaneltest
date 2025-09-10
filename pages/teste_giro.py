import streamlit as st
import pandas as pd
import requests




# -------------------------------
# CONFIGURAÇÃO DA PÁGINA
# -------------------------------
st.set_page_config(
    page_title="Dashboard Google Sheets",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Dashboard de Planilha Google Sheets")

# -------------------------------
# LINK DA PLANILHA CSV
# -------------------------------
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTRuYovKK1C-FEzJDE5CzN5cubXHqZuXzGzvD69XQa7Lj15PKZfmmzyRC8zpyjhq7hst0yEYHJdWYYM/pub?gid=0&single=true&output=csv"

# -------------------------------
# LER PLANILHA
# -------------------------------
@st.cache_data  # para cache e evitar recarregar sempre
def load_data(url):
    df = pd.read_csv(url)
    return df

df = load_data(url)

# -------------------------------
# FILTROS INTERATIVOS
# -------------------------------
st.sidebar.header("Filtros")

# Busca rápida em todas as colunas
search = st.text_input("🔍 Buscar")
if search:
    df = df[df.apply(lambda row: row.astype(str).str.contains(search, case=False).any(), axis=1)]

# -------------------------------
# EXIBIÇÃO DA TABELA
# -------------------------------
st.subheader("Testes de Giro")

# Criar uma cópia sem as colunas de imagem
df_exibir = df.drop(columns=["Antes", "Depois"], errors="ignore")

st.dataframe(df_exibir)


@st.cache_data(show_spinner=False)
def request_image(coluna):
    url_antes = str(row.get(coluna, "")).strip()
    response = requests.get(url_antes)
    return response.content

# Exemplo: filtro por coluna
for i, row in df.iterrows():
    if pd.notna(row["Mudança"]) and str(row["Mudança"]).strip() != "":
        with st.expander(f"Mudança aplicada no Teste {row['ID Teste']} - {row['Mudança']}"):
            st.write(f"**Data:** {row['Data']}")
            st.write(f"**Alvo:** {row['Alvo']}")
            st.write(f"**Resultado:** {row['Resultado']}")
            st.write(f"**Observações:** {row['Observações']}")
            st.write(f"**Descrição da mudança:** {row['Mudança']}")
            
            # Colunas lado a lado para antes e depois
            
            col1, col2 = st.columns(2)
              # Imagem "Antes"
            with col1:
                st.image(request_image("Antes"), caption="Antes", width=300)

            # Imagem "Depois"
            with col2:
                st.image(request_image("Depois"), caption="Depois", width=300)
