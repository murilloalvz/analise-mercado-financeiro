# Análise de Mercado Financeiro 📈

Dashboard interativo desenvolvido em Python para consultar dados reais do mercado financeiro, analisar um ativo principal e comparar seu desempenho com um benchmark ou outro ativo.

O projeto reúne coleta de séries históricas, tratamento de dados, indicadores de retorno e risco, médias móveis e visualizações em uma interface construída com Streamlit. Além da análise financeira, o desenvolvimento também pratica organização modular, separação de responsabilidades e versionamento com Git/GitHub.

## Funcionalidades atuais

- Consulta de séries históricas com `yfinance`
- Interface interativa com Streamlit
- Seleção dinâmica do ativo principal
- Seleção de benchmark / ativo de comparação
- Seleção do período de análise: 1 mês, 3 meses, 6 meses, 1 ano, 2 anos ou 5 anos
- Validação quando um dos ativos não retorna dados
- Cálculo do preço inicial e atual
- Cálculo do retorno percentual no período
- Cálculo do retorno diário
- Média do retorno diário
- Volatilidade diária
- Médias móveis de 20 e 50 períodos
- Aviso quando o histórico é insuficiente para visualizar adequadamente a média móvel de 50 períodos
- Gráfico de evolução do preço com MM20 e MM50
- Normalização dos preços para comparação entre ativos com escalas diferentes
- Gráfico comparativo de desempenho normalizado
- Comparação de retorno e volatilidade entre o ativo principal e o benchmark
- Cálculo do desempenho relativo em pontos percentuais
- Indicação de quando o ativo principal superou, igualou ou ficou abaixo do benchmark

## Tecnologias

- Python
- Pandas
- yfinance
- Matplotlib
- Streamlit
- Git e GitHub

## Estrutura do projeto

```text
analise-mercado-financeiro/
├── app.py              # Interface e orquestração da aplicação Streamlit
├── src/
│   ├── data.py         # Coleta e preparação inicial dos dados financeiros
│   ├── analysis.py     # Retornos, estatísticas, médias móveis e comparação
│   └── charts.py       # Gráficos de preço e comparação normalizada
├── .gitignore
├── requirements.txt
└── README.md
```

## Fluxo da aplicação

```text
Ativo principal + benchmark + período
                 ↓
          Coleta com yfinance
                 ↓
       Validação e preparação
                 ↓
     ┌───────────┴───────────┐
     ↓                       ↓
Ativo principal          Benchmark
     ↓                       ↓
Retorno e risco          Retorno e risco
Médias móveis            Normalização
Normalização                 ↓
     └───────────┬───────────┘
                 ↓
      Comparação de desempenho
                 ↓
       Dashboard no Streamlit
```

## Análises disponíveis

### Ativo principal

O dashboard apresenta o retorno no período, média do retorno diário, volatilidade diária, preço inicial, preço atual e um gráfico com o preço de fechamento acompanhado pelas médias móveis de 20 e 50 períodos.

### Comparação com benchmark

O usuário pode informar um segundo ativo para servir como benchmark ou referência. Os preços são normalizados para uma base comum, permitindo comparar a evolução relativa mesmo quando os ativos possuem preços nominais ou moedas diferentes.

A aplicação também compara retorno e volatilidade e calcula o desempenho relativo do ativo principal em relação ao benchmark, apresentado em pontos percentuais.

## Como executar

Clone o repositório:

```bash
git clone https://github.com/murilloalvz/analise-mercado-financeiro.git
cd analise-mercado-financeiro
```

Crie um ambiente virtual:

```bash
python -m venv venv
```

Ative o ambiente virtual.

Windows:

```bash
.\venv\Scripts\activate
```

Linux ou macOS:

```bash
source venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute a aplicação:

```bash
streamlit run app.py
```

Depois, informe o ativo principal, o benchmark e o período desejado pela barra lateral da aplicação.

### Exemplos de tickers

```text
PETR4.SA  → Petrobras
VALE3.SA  → Vale
BOVA11.SA → ETF do Ibovespa
AAPL      → Apple
MSFT      → Microsoft
NVDA      → NVIDIA
SPY       → ETF do S&P 500
```

## Conceitos praticados

Durante o desenvolvimento, o projeto trabalha conceitos de Python, análise de dados e organização de software, incluindo:

- Funções, parâmetros, argumentos e `return`
- Módulos próprios e imports
- DataFrames e Series
- Indexação com `iloc`
- Tratamento de MultiIndex
- Criação e transformação de colunas
- `pct_change()`, `mean()`, `std()` e `rolling()`
- Normalização de séries temporais
- Desempacotamento de valores
- Controle de fluxo e validação de dados
- Separação de responsabilidades entre coleta, análise, visualização e interface
- Visualização de séries temporais com Matplotlib
- Desenvolvimento de dashboards com Streamlit
- Versionamento incremental com Git/GitHub

## Roadmap para a v1.0

- [x] Estruturar o repositório
- [x] Coletar séries históricas com `yfinance`
- [x] Calcular retorno do período e retornos diários
- [x] Calcular média e volatilidade diária
- [x] Adicionar médias móveis de 20 e 50 períodos
- [x] Criar visualização de preço e médias móveis
- [x] Separar coleta, análise e visualização em módulos
- [x] Criar interface interativa com Streamlit
- [x] Permitir seleção dinâmica de ativo e período
- [x] Adicionar ativo de comparação / benchmark
- [x] Normalizar preços para comparação
- [x] Comparar retorno e volatilidade
- [x] Calcular desempenho relativo ao benchmark
- [ ] Realizar revisão final de UX e casos extremos
- [ ] Revisar e refatorar o código para publicação
- [ ] Adicionar screenshots e finalizar a documentação
- [ ] Publicar/deployar a versão v1.0

## Status

🚧 **Em fase final de desenvolvimento da v1.0.**

O núcleo de análise e comparação já está funcional. Os próximos passos estão focados em testes, polimento da interface, revisão técnica e preparação da versão pública do projeto.

## Autor

**Murillo Lourenço**  
Estudante de Análise e Desenvolvimento de Sistemas na FATEC Sorocaba.

Interesses: Dados, Inteligência Artificial, Automação e Mercado Financeiro.
