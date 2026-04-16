import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

# conexão
engine = create_engine('postgresql://postgres:1234@localhost:5432/iot')

def load(view):
    return pd.read_sql(f"SELECT * FROM {view}", engine)

# config página
st.set_page_config(page_title="IoT Dashboard", layout="wide")

# título
st.title("🌡️ IoT Temperature Dashboard")
st.markdown("Análise de dados de sensores de temperatura")

# carregar dados
df1 = load('avg_temp_por_dispositivo')
df2 = load('leituras_por_hora')
df3 = load('temp_max_min_por_dia')

# métricas rápidas
col1, col2, col3 = st.columns(3)

col1.metric("Dispositivos", df1.shape[0])
col2.metric("Maior Temp", f"{df3['temp_max'].max()}°C")
col3.metric("Menor Temp", f"{df3['temp_min'].min()}°C")

st.divider()

# gráficos lado a lado
col1, col2 = st.columns(2)

with col1:
    fig1 = px.bar(
        df1,
        x='device_id',
        y='avg_temp',
        title="🌡️ Média de Temperatura por Dispositivo"
    )
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    fig2 = px.line(
        df2,
        x='hora',
        y='contagem',
        title="⏱️ Leituras por Hora"
    )
    st.plotly_chart(fig2, use_container_width=True)

# gráfico principal
st.subheader("📅 Temperaturas Máximas e Mínimas por Dia")

fig3 = px.line(
    df3,
    x='data',
    y=['temp_max', 'temp_min'],
    markers=True
)

st.plotly_chart(fig3, use_container_width=True)