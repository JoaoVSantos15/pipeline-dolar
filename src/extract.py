import requests
import logging

# Configuração básica de log para vermos o que acontece
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def fetch_currency_data():
    """
    Busca a cotação atual do Dólar (USD) para Real (BRL) na AwesomeAPI.
    Retorna o dicionário com os dados ou levanta uma exceção em caso de erro.
    """
    url = "https://economia.awesomeapi.com.br/last/USD-BRL"
    
    try:
        logging.info("Iniciando requisição para a AwesomeAPI...")
        response = requests.get(url, timeout=10)
        
        # Verifica se o status code é 200 (Sucesso)
        response.raise_for_status()
        
        data = response.json()
        logging.info("Dados extraídos com sucesso da API.")
        return data['USDBRL']
        
    except requests.exceptions.HTTPError as http_err:
        logging.error(f"Erro HTTP encontrado: {http_err}")
        raise
    except requests.exceptions.ConnectionError as conn_err:
        logging.error(f"Erro de conexão. Verifique sua internet: {conn_err}")
        raise
    except Exception as err:
        logging.error(f"Um erro inesperado ocorreu: {err}")
        raise