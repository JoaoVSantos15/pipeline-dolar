import requests
import logging

# Configuração básica de log para vermos o que acontece
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def fetch_currency_data(moedas_list):
    query = ",".join(moedas_list)
    url = f"https://economia.awesomeapi.com.br/last/{query}"
    
    try:
        logging.info(f"Iniciando requisição para a AwesomeAPI: {query}")
        # Definir um timeout é uma boa prática de segurança/resiliência
        response = requests.get(url, timeout=10)
        
        # Verifica se o status code é 200 (Sucesso)
        response.raise_for_status()
        
        data = response.json()
        logging.info("Dados extraídos com sucesso da API.")
        return data

    except requests.exceptions.HTTPError as http_err:
        logging.error(f"Erro HTTP encontrado: {http_err}")
        raise
    except requests.exceptions.ConnectionError as conn_err:
        logging.error(f"Erro de conexão. Verifique sua internet: {conn_err}")
        raise
    except Exception as err:
        logging.error(f"Um erro inesperado ocorreu: {err}")
        raise