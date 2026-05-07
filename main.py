from src.extract import fetch_currency_data
from src.transform import transform_currency_data
from src.load import save_to_parquet
import logging

# Configuração de Log Centralizada
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def run_pipeline():
    try:
        # 1. EXTRAÇÃO (Bronze)
        raw_data = fetch_currency_data()
        
        # 2. TRANSFORMAÇÃO (Silver)
        df = transform_currency_data(raw_data)
        
        # 3. CARGA (Gold/Refined)
        save_to_parquet(df)
        
        logging.info("Pipeline executada com sucesso!")
        
    except Exception as e:
        logging.error(f"A pipeline falhou durante a execução: {e}")

if __name__ == "__main__":
    run_pipeline()