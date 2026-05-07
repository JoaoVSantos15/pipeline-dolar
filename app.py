import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

# 1. Descobrir onde o app.py está localizado
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 2. Montar o caminho para o arquivo parquet dentro da pasta data
# Isso garante que ele aponte para pipeline/data/cotacao_dolar.parquet
PATH_PARQUET = os.path.join(BASE_DIR, "data", "cotacao_dolar.parquet")

st.set_page_config(page_title="Dashboard Intelligence", layout="wide")

@st.cache_data
def load_data():
    df = pd.read_parquet("data/cotacao_dolar.parquet")
    df['data_consulta'] = pd.to_datetime(df['data_consulta'])
    # Garantir que os dados estão em ordem cronológica para a média móvel
    df = df.sort_values('data_consulta')
    return df

try:
    data = load_data()
    st.title("Business Intelligence: Cotações e Tendências")

    # Sidebar
    moeda_selecionada = st.sidebar.selectbox("Selecione a Moeda", data['moeda_origem'].unique())
    janela_media = st.sidebar.slider("Janela da Média Móvel (registros)", 2, 20, 5)

    # Filtragem
    df_filtrado = data[data['moeda_origem'] == moeda_selecionada].copy()
    
    # Cálculo de Média Móvel (Storytelling)
    df_filtrado['media_movel'] = df_filtrado['compra'].rolling(window=janela_media).mean()

    # Métricas
    if not df_filtrado.empty:
        ultima = df_filtrado.iloc[-1]
        col1, col2, col3 = st.columns(3)
        col1.metric("Preço Atual", f"R$ {float(ultima['compra']):.2f}")
        col2.metric("Média Móvel", f"R$ {float(ultima['media_movel']):.2f}" if not pd.isna(ultima['media_movel']) else "Calculando...")
        col3.metric("Variação do Dia", f"{float(ultima['variacao_pct']):.4f}%")

        # Gráfico Avançado com Plotly Graph Objects
        st.subheader(f"Análise de Tendência - {moeda_selecionada}")
        fig = go.Figure()
        
        # Linha do Preço Real
        fig.add_trace(go.Scatter(x=df_filtrado['data_consulta'], y=df_filtrado['compra'],
                                 mode='lines+markers', name='Preço Real', line=dict(color='#00CC96')))
        
        # Linha da Média Móvel
        fig.add_trace(go.Scatter(x=df_filtrado['data_consulta'], y=df_filtrado['media_movel'],
                                 mode='lines', name='Tendência (Média)', line=dict(color='#EF553B', dash='dash')))

        fig.update_layout(template="plotly_dark", hovermode="x unified")
        st.plotly_chart(fig, use_container_width=True)

except Exception as e:
    st.error(f"Erro ao processar dashboard: {e}")