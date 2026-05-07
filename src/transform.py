import pandas as pd
import logging

def transform_currency_data(raw_data):
    """
    Recebe o dicionário bruto da API, limpa, renomeia colunas 
    e garante a tipagem correta para análise de BI.
    """
    try:
        logging.info("Iniciando transformação dos dados...")
        
        # Converter o dicionário para DataFrame
        df = pd.DataFrame([raw_data])
        
        # Selecionar apenas colunas interessantes (Filtragem)
        columns_to_keep = ['code', 'codein', 'bid', 'ask', 'pctChange', 'create_date']
        df = df[columns_to_keep]
        
        # Renomear colunas para algo mais intuitivo (Padronização)
        df.columns = ['moeda_origem', 'moeda_destino', 'compra', 'venda', 'variacao_pct', 'data_consulta']
        
        # CORREÇÃO DE TIPAGEM (Essencial para BI)
        # O valor vem da API como texto (string). Precisamos de Float para fazer cálculos.
        cols_financeiras = ['compra', 'venda', 'variacao_pct']
        for col in cols_financeiras:
            df[col] = pd.to_numeric(df[col])
            
        # Converter a data de string para objeto DateTime
        df['data_consulta'] = pd.to_datetime(df['data_consulta'])
        
        # Adicionar uma coluna de metadado: Data de Processamento (Audit)
        df['processado_em'] = pd.to_datetime('now')
        
        logging.info("Transformação concluída com sucesso.")
        return df
        
    except Exception as e:
        logging.error(f"Erro na transformação de dados: {e}")
        raise