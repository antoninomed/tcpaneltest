import streamlit as st
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
from sklearn.cluster import KMeans
import plotly.express as px

# -------------------------------
# Configuração da página
# -------------------------------
st.set_page_config(
    page_title="Dashboard de Rounds do Robô",
    layout="wide"
)

# -------------------------------
# Carregar Planilha
# -------------------------------
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTRuYovKK1C-FEzJDE5CzN5cubXHqZuXzGzvD69XQa7Lj15PKZfmmzyRC8zpyjhq7hst0yEYHJdWYYM/pub?gid=1674634257&single=true&output=csv"

@st.cache_data
def load_data(url):
    df = pd.read_csv(url)
    return df

df = load_data(url)
df['Data'] = pd.to_datetime(df['Data'], dayfirst=True).dt.date

st.title("📊 Dashboard de Rounds do Robô")

# -------------------------------
# Sidebar - Filtros
# -------------------------------
st.sidebar.header("Filtros")
# Seleção de missões
colunas_missoes = st.sidebar.multiselect(
    "Selecione as missões:",
    options=[c for c in df.columns if "M" in c],
    default=[c for c in df.columns if "M" in c]
)

# Filtro de datas
min_data, max_data = df['Data'].min(), df['Data'].max()
data_inicio = st.sidebar.date_input("Data Início", min_data)
data_fim = st.sidebar.date_input("Data Fim", max_data)

# Aplicar filtros
df_filtrado = df[df['Data'].between(data_inicio, data_fim)]
if len(colunas_missoes) > 0:
    df_missoes = df_filtrado[colunas_missoes]
else:
    st.warning("Selecione pelo menos uma missão para análise.")
    st.stop()

# -------------------------------
# Transformar em binário de falha (0 = falhou, 1 = completou)
# -------------------------------
df_bin = df_missoes.applymap(lambda x: 1 if x > 0 else 0)
df_fail = 1 - df_bin  # 1 = falha

# -------------------------------
# Painel 1: Tabela de Rounds
# -------------------------------
st.subheader("📋 Tabela de Rounds Filtrada")
st.dataframe(df_filtrado[[*colunas_missoes, 'Data']])

# -------------------------------
# Painel 2: Ranking das Missões Mais Problemáticas
# -------------------------------
st.subheader("🔥 Ranking das Missões Mais Problemáticas")
falha_pct = df_fail.mean().sort_values(ascending=False) * 100
ranking = pd.DataFrame({'Missão': falha_pct.index, 'Percentual de Falha': falha_pct.values})
st.dataframe(ranking)

# Gráfico de barras
fig_ranking = px.bar(
    ranking,
    x='Missão',
    y='Percentual de Falha',
    text='Percentual de Falha',
    title="Missões com Maior Percentual de Falha",
    color='Percentual de Falha',
    color_continuous_scale='Reds'
)
st.plotly_chart(fig_ranking, use_container_width=True)


