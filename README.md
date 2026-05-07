# Financial Data Pipeline & BI Dashboard

Este projeto é uma pipeline de dados (ETL) automatizada que extrai cotações de moedas (Dólar, Euro e Bitcoin), armazena-as em um formato de alta performance (Parquet) e as visualiza em um dashboard interativo para análise de tendências.

## Tecnologias Utilizadas
- **Linguagem:** Python 3.x
- **Extração:** API AwesomeAPI (JSON)
- **Processamento/Análise:** Pandas & Numpy
- **Armazenamento:** Apache Parquet (Storage colunar para BI)
- **Visualização:** Streamlit & Plotly
- **Automação:** GitHub Actions (CI/CD)

## Estrutura do Projeto
```text
pipeline/
├── .github/workflows/  # Automação de execução programada
├── data/               # Local de armazenamento do Data Lake (Parquet)
├── src/                # Scripts modulares (Extract, Transform, Load)
├── main.py             # Executável principal da Pipeline
└── app.py              # Dashboard interativo do Streamlit

## Funcionalidades

### Multi-Moedas: Monitoramento simultâneo de USD, EUR e BTC.

### Data Lake Resiliente: Acúmulo de dados históricos sem duplicidade.

### Análise de Tendência: Dashboard com Média Móvel configurável para suavizar ruídos de mercado (especialmente útil para criptomoedas).

### Segurança: Uso de variáveis de ambiente e caminhos relativos para portabilidade total.

## Como Executar

### Clone o repositório:

git clone [https://github.com/JoaoVSantos15/pipeline-cotacao.git](https://github.com/JoaoVSantos15/pipeline-cotacao.git)
cd pipeline-cotacao

## Instale as dependências:

pip install -r requirements.txt

## Execute a Pipeline (Extração):

python pipeline/main.py

## Inicie o Dashboard:

python -m streamlit run pipeline/app.py

## Automação (GitHub Actions)

O projeto está configurado para rodar automaticamente em intervalos programados, garantindo que o dashboard esteja sempre atualizado com os dados mais recentes do mercado sem intervenção humana.