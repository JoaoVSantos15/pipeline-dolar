# Pipeline de Cotação de Dólar (ETL)

Pipeline automatizada para extração, transformação e armazenamento de cotações USD-BRL utilizando Python e GitHub Actions.

## Tecnologias Utilizadas
- **Python 3.11**
- **Pandas**: Manipulação e transformação de dados.
- **PyArrow**: Engine para suporte ao formato Parquet.
- **GitHub Actions**: Automação da pipeline (CI/CD).
- **AwesomeAPI**: Fonte de dados em tempo real.

## Arquitetura
O projeto segue o modelo de responsabilidade única:
1. **Extract**: Captura dados brutos da API com tratamento de erros e timeouts.
2. **Transform**: Limpeza, renomeação de colunas e tipagem correta (float/datetime).
3. **Load**: Armazenamento incremental em formato **Parquet** (colunar), garantindo performance e histórico sem duplicatas.

## Automação
A pipeline está configurada para rodar automaticamente todos os dias através do GitHub Actions, mantendo o arquivo de dados sempre atualizado no repositório.