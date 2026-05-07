import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard Multimoedas", layout="wide")

@st.cache_data
def load_data():
    df = pd.read_parquet("data/cotacao_dolar.parquet")
    df['data_consulta'] = pd.to_datetime(df['data_consulta'])
    return df

try:
    data = load_data()
    
    # --- ÁREA DE DEBUG (Remover depois) ---
    st.sidebar.write(f"Total de registros no arquivo: {len(data)}")
    st.sidebar.write(f"Moedas encontradas: {data['moeda_origem'].unique()}")
    # ---------------------------------------

    st.title("📊 Monitoramento Multimoedas")

    # Filtro Dinâmico
    lista_moedas = data['moeda_origem'].unique()
    moeda_selecionada = st.sidebar.selectbox("Selecione a Moeda", lista_moedas)

    # Filtrando os dados com base na seleção
    df_filtrado = data[data['moeda_origem'] == moeda_selecionada]
    
    if not df_filtrado.empty:
        ultima_cotacao = df_filtrado.iloc[-1]
        
        col1, col2, col3 = st.columns(3)
        col1.metric(f"Compra ({moeda_selecionada})", f"R$ {float(ultima_cotacao['compra']):.2f}")
        col2.metric("Venda", f"R$ {float(ultima_cotacao['venda']):.2f}")
        col3.metric("Variação", f"{ultima_cotacao['variacao_pct']}%")

        st.subheader(f"Evolução Histórica - {moeda_selecionada}")
        fig = px.line(df_filtrado, x='data_consulta', y='compra', markers=True)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("Nenhum dado encontrado para a moeda selecionada.")

except Exception as e:
    st.error(f"Erro: {e}")