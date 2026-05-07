import pandas as pd
import os
import logging

def save_to_parquet(df, filename="data/cotacao_dolar.parquet"):
    """
    Salva o DataFrame em formato Parquet. 
    Se o arquivo já existir, anexa os novos dados ao histórico.
    """
    try:
        logging.info(f"Iniciando persistência dos dados em {filename}...")
        
        # Criar a pasta data se ela não existir (Prevenção de erros)
        os.makedirs(os.path.dirname(filename), exist_ok=True)

        if os.path.exists(filename):
            logging.info("Arquivo existente encontrado. Lendo histórico...")
            # Lemos o histórico
            df_historical = pd.read_parquet(filename)
            # Concatenamos o novo dado
            df_final = pd.concat([df_historical, df], ignore_index=True)
            # Removemos duplicatas (caso o script rode duas vezes no mesmo minuto)
            df_final = df_final.drop_duplicates(subset=['data_consulta'])
        else:
            logging.info("Nenhum arquivo existente encontrado. Criando novo histórico...")
            df_final = df
        
        # Salvar em Parquet usando compressão Snappy (padrão de mercado)
        df_final.to_parquet(filename, index=False, compression='snappy')
        logging.info(f"Dados salvos com sucesso! Total de registros: {len(df_final)}")
        
    except Exception as e:
        logging.error(f"Erro ao salvar em Parquet: {e}")
        raise