import os
import logging
from src.extract import fetch_currency_data
from src.transform import transform_currency_data
from src.load import save_to_parquet

# Configuração de Logs
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def run_pipeline():
    # Ponto de Segurança: Busca o caminho do cofre ou usa o padrão
    # Pega o caminho absoluto de onde o arquivo main.py está
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    # Define o caminho para a pasta data dentro da pasta do script
    # Se o seu main.py está em 'pipeline/', o data será criado em 'pipeline/data/'
    target_file = os.path.join(BASE_DIR, "data", "cotacao_dolar.parquet")

    # Garante que a pasta 'data' existe antes de salvar
    os.makedirs(os.path.dirname(target_file), exist_ok=True)

    # Configuração de Expansão: Lista de moedas que queremos monitorar
    # O formato da AwesomeAPI é 'MoedaOrigem-MoedaDestino'
    currencies = ["USD-BRL", "EUR-BRL", "BTC-BRL"]
    
    try:
        logging.info(f"Iniciando pipeline para as moedas: {currencies}")
        
        # 1. Extração (Agora enviando a lista completa)
        raw_data = fetch_currency_data(currencies)
        
        if raw_data:
            all_processed_data = []
            
            # 2. Transformação (Iteramos sobre cada moeda retornada pela API)
            for key in raw_data:
                logging.info(f"Processando dados para: {key}")
                df_item = transform_currency_data(raw_data[key])
                all_processed_data.append(df_item)
            
            # Unificamos todas as moedas em um único DataFrame
            import pandas as pd
            final_df = pd.concat(all_processed_data, ignore_index=True)
            
            # 3. Carga (Salvando o novo "Data Lake" unificado)
            save_to_parquet(final_df, target_file)
            logging.info("Pipeline multimoedas executada com sucesso!")
        
    except Exception as e:
        logging.error(f"Erro crítico na pipeline: {e}")

if __name__ == "__main__":
    run_pipeline()