import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração da página
st.set_page_config(page_title="Dashboard Cotação Dólar", layout="wide")

st.title("📊 Monitoramento de Cotação: Dólar (USD) para Real (BRL)")

# Função para carregar os dados
@st.cache_data
def load_data():
    # Caminho do arquivo que sua pipeline gera
    df = pd.read_parquet("data/cotacao_dolar.parquet")
    # Garante que a data está no formato correto
    df['data_consulta'] = pd.to_datetime(df['data_consulta'])
    return df

try:
    data = load_data()

    # Filtros na barra lateral
    st.sidebar.header("Filtros")
    moeda = st.sidebar.selectbox("Selecione a Moeda", data['moeda_origem'].unique())

    # Métricas Principais
    ultima_cotacao = data.iloc[-1]
    col1, col2, col3 = st.columns(3)
    
    col1.metric("Valor de Compra", f"R$ {ultima_cotacao['compra']:.2f}")
    col2.metric("Valor de Venda", f"R$ {ultima_cotacao['venda']:.2f}")
    col3.metric("Variação (%)", f"{ultima_cotacao['variacao_pct']}%")

    # Gráfico de Evolução
    st.subheader("Evolução do Preço ao Longo do Tempo")
    fig = px.line(data, x='data_consulta', y='compra', 
                  title=f"Histórico de Compra - {moeda}",
                  labels={'data_consulta': 'Data da Consulta', 'compra': 'Preço (R$)'},
                  markers=True)
    st.plotly_chart(fig, use_container_width=True)

    # Tabela de Dados
    st.subheader("Dados Brutos")
    st.dataframe(data.sort_values(by='data_consulta', ascending=False), use_container_width=True)

except Exception as e:
    st.error(f"Erro ao carregar dados: {e}")
    st.info("Certifique-se de que o arquivo 'data/cotacao_dolar.parquet' existe.")