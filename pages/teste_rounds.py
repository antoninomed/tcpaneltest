import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------------------
# Upload da planilha
# -------------------------------
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTRuYovKK1C-FEzJDE5CzN5cubXHqZuXzGzvD69XQa7Lj15PKZfmmzyRC8zpyjhq7hst0yEYHJdWYYM/pub?gid=1674634257&single=true&output=csv"

# -------------------------------
# LER PLANILHA
# -------------------------------
@st.cache_data
def load_data(url):
    df = pd.read_csv(url)
    df['Data'] = pd.to_datetime(df['Data'], dayfirst=True).dt.date
    return df

df = load_data(url)

# -------------------------------
# FILTRO DE DATA NA SIDEBAR
# -------------------------------
st.sidebar.header("Filtros")
min_date = df['Data'].min()
max_date = df['Data'].max()

data_range = st.sidebar.date_input(
    "Selecione o período:",
    value=[min_date, max_date],
    min_value=min_date,
    max_value=max_date
)

# Garantir que data_range seja lista de duas datas
if isinstance(data_range, tuple):
    start_date, end_date = data_range
else:
    start_date, end_date = min_date, max_date

# Filtrar o DataFrame
df_filtrado = df[(df['Data'] >= start_date) & (df['Data'] <= end_date)]

# -------------------------------
# Tabela de Rounds
# -------------------------------
st.subheader("Tabela de Rounds")
st.dataframe(df_filtrado)

# -------------------------------
# Evolução da pontuação total
# -------------------------------
st.subheader("Evolução da Pontuação Total")
fig_total = px.line(
    df_filtrado,
    x='Data',
    y='Total',
    markers=True,
    title="Pontuação Total ao longo do tempo",
    range_y=[0, 545]
)
st.plotly_chart(fig_total, use_container_width=True)

# -------------------------------
# Eficiência por missão (%)
# -------------------------------
st.subheader("Eficiência por missão (%)")

missoes = [col for col in df_filtrado.columns if col.startswith('M')]

maximos = {'M01': 20, 'M02': 30, 'M03': 30}
for m in missoes:
    if m not in maximos:
        maximos[m] = 30

precisao = {}
for m in missoes:
    precisao[m] = df_filtrado[m].sum() / (len(df_filtrado) * maximos[m]) * 100

precisao_df = pd.DataFrame({'Missão': precisao.keys(), 'Precisão (%)': precisao.values()}).sort_values(by='Precisão (%)', ascending=False)

# Mostrar tabela e gráfico lado a lado
col1, col2 = st.columns(2)

with col1:
    st.dataframe(precisao_df)

with col2:
    fig_precisao = px.bar(
        precisao_df,
        x='Missão',
        y='Precisão (%)',
        text='Precisão (%)',
        title="Precisão Média de Acertos por Missão",
        color='Precisão (%)',
        color_continuous_scale='Blues'
    )
    st.plotly_chart(fig_precisao, use_container_width=True)

# -------------------------------
# Análise detalhada por missão
# -------------------------------
st.subheader("Análise detalhada por missão")
selected_missao = st.selectbox("Escolha a missão", missoes)

fig_single = px.line(
    df_filtrado,
    x='Data',
    y=selected_missao,
    markers=True,
    title=f"Pontuação da {selected_missao} ao longo do tempo",
    range_y=[0, maximos[selected_missao]]
)
st.plotly_chart(fig_single, use_container_width=True)

# -------------------------------
# Assistente de IA com insights e recomendações
# -------------------------------

# 1️⃣ Missões com melhor e pior desempenho
melhor_missao = precisao_df.loc[precisao_df['Precisão (%)'].idxmax()]
pior_missao = precisao_df.loc[precisao_df['Precisão (%)'].idxmin()]

# 2️⃣ Tendência da pontuação total
if len(df_filtrado) > 1:
    total_diff = df_filtrado['Total'].iloc[-1] - df_filtrado['Total'].iloc[0]
    if total_diff > 0:
        tendencia = "subindo 📈"
    elif total_diff < 0:
        tendencia = "caindo 📉"
    else:
        tendencia = "estável ➖"
else:
    tendencia = "sem dados suficientes para avaliar"

# 3️⃣ Missão mais irregular
desvios = {m: df_filtrado[m].std() for m in missoes}
missao_irregular = max(desvios, key=desvios.get)

# 4️⃣ Recomendações automáticas
recomendacoes = []

# Sugestão baseada em pior missão
if pior_missao['Precisão (%)'] < 50:
    recomendacoes.append(f"💡 Focar em treinar a missão **{pior_missao['Missão']}**, que tem baixa precisão ({pior_missao['Precisão (%)']:.1f}%).")

# Sugestão baseada em tendência
if total_diff < 0:
    recomendacoes.append("⚠️ A pontuação total está caindo, analisar causas e ajustar estratégia de treinos.")
elif total_diff > 0:
    recomendacoes.append("✅ A pontuação total está melhorando, continue mantendo a estratégia atual.")

# Sugestão baseada em irregularidade
if desvios[missao_irregular] > 5:
    recomendacoes.append(f"⚡ A missão **{missao_irregular}** é a mais irregular (desvio padrão {desvios[missao_irregular]:.1f}), priorizar consistência nos treinos.")

# Sugestão para missões quase perfeitas
for m in missoes:
    if precisao[m] > 90:
        recomendacoes.append(f"🏆 A missão **{m}** está com desempenho excelente, manter a prática atual.")

st.markdown("### Crew Assistente")
for r in recomendacoes:
    st.markdown(f"- {r}")
