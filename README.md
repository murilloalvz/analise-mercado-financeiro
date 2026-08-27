# Análise de Mercado Financeiro

Dashboard de **análise de séries temporais financeiras** desenvolvido em Python para consultar dados reais de mercado, avaliar retorno e risco e comparar um ativo com um benchmark.

O projeto combina aquisição de dados externos, transformação com Pandas, indicadores quantitativos e visualização em uma interface Streamlit.

## O que este projeto demonstra

- Consumo e tratamento de dados financeiros externos
- Manipulação de séries temporais com Pandas
- Cálculo de retorno, volatilidade e médias móveis
- Normalização de séries para comparação entre ativos
- Análise relativa contra benchmark
- Visualização de dados com Matplotlib
- Arquitetura modular separando dados, análise, gráficos e interface

## Funcionalidades

- Consulta de séries históricas com `yfinance`
- Seleção dinâmica de ativo e benchmark
- Períodos de 1 mês a 5 anos
- Validação de ativos sem dados
- Preço inicial e atual
- Retorno percentual do período
- Retornos diários e retorno diário médio
- Volatilidade diária
- Médias móveis de 20 e 50 períodos
- Gráfico de preço com médias móveis
- Normalização de preços
- Comparação visual entre ativo e benchmark
- Comparação de retorno e volatilidade
- Desempenho relativo em pontos percentuais

## Stack

**Python • Pandas • yfinance • Matplotlib • Streamlit • Git/GitHub**

## Arquitetura

```text
Ativo + benchmark + período
            ↓
     yfinance / dados
            ↓
 Validação e preparação
            ↓
 ┌──────────┴──────────┐
 ↓                     ↓
Ativo              Benchmark
 ↓                     ↓
Retorno / risco    Retorno / risco
MM20 / MM50        Normalização
 └──────────┬──────────┘
            ↓
   Análise comparativa
            ↓
 Dashboard Streamlit
```

## Estrutura

```text
analise-mercado-financeiro/
├── app.py
├── src/
│   ├── data.py       # coleta e preparação
│   ├── analysis.py   # indicadores e comparação
│   └── charts.py     # visualizações
├── .gitignore
├── requirements.txt
└── README.md
```

## Análises disponíveis

### Retorno e risco

O dashboard calcula retorno no período, média do retorno diário e volatilidade diária, além de exibir preços inicial e atual.

### Tendência

O preço de fechamento é visualizado junto às médias móveis de 20 e 50 períodos. A aplicação informa quando não existe histórico suficiente para interpretar adequadamente a MM50.

### Benchmark

As séries são normalizadas para uma base comum antes da comparação, evitando que diferenças de preço nominal impeçam a análise relativa. O dashboard compara retorno, volatilidade e desempenho relativo em pontos percentuais.

## Executando localmente

```bash
git clone https://github.com/murilloalvz/analise-mercado-financeiro.git
cd analise-mercado-financeiro
python -m venv venv
```

Windows:

```bash
.\venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

Depois:

```bash
pip install -r requirements.txt
streamlit run app.py
```

Exemplos de ativos: `PETR4.SA`, `VALE3.SA`, `BOVA11.SA`, `AAPL`, `MSFT`, `NVDA` e `SPY`.

## Conceitos aplicados

O desenvolvimento trabalha DataFrames e Series, indexação, transformação de colunas, `pct_change()`, `mean()`, `std()`, `rolling()`, normalização de séries temporais, validação de dados e separação de responsabilidades.

## Status da v1.0

O núcleo de análise e comparação está funcional. A etapa final está concentrada em revisão de UX, casos extremos, refatoração, screenshots e deploy.

- [x] Coleta de séries históricas
- [x] Retorno e retornos diários
- [x] Volatilidade
- [x] Médias móveis
- [x] Arquitetura modular
- [x] Interface Streamlit
- [x] Benchmark e normalização
- [x] Comparação de retorno e risco
- [ ] Revisão final e casos extremos
- [ ] Screenshots
- [ ] Deploy v1.0

## Autor

**Murillo Lourenço**  
ADS — FATEC Sorocaba

Foco em Dados, Inteligência Artificial, Automação e aplicações financeiras.
