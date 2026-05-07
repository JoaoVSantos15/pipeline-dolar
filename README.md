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