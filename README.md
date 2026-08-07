# Análise do Mercado Financeiro

Projeto em desenvolvimento para coletar, transformar e analisar dados reais do mercado financeiro com Python.

A proposta é construir um fluxo completo de análise, partindo da obtenção de séries históricas até o cálculo de indicadores e a criação de visualizações. O projeto também serve como prática de organização de código, uso de módulos e versionamento com Git/GitHub.

## Funcionalidades atuais

- Coleta de séries históricas de ativos com `yfinance`
- Seleção de ativo e período de análise
- Validação para evitar cálculos quando não há dados retornados
- Normalização das colunas recebidas do `yfinance`
- Cálculo do primeiro e do último preço de fechamento do período
- Cálculo do retorno percentual do período
- Cálculo do retorno diário com `pct_change()`
- Cálculo da média do retorno diário
- Cálculo da volatilidade diária por meio do desvio padrão
- Médias móveis de 20 e 50 períodos com `rolling()`
- Gráfico com preço de fechamento e médias móveis usando Matplotlib
- Código separado em módulos de coleta, análise e visualização

## Tecnologias

- Python
- Pandas
- NumPy
- yfinance
- Matplotlib
- Git e GitHub

## Estrutura atual

```text
analise-mercado-financeiro/
├── data/
├── images/
├── src/
│   ├── main.py       # Orquestra o fluxo da aplicação
│   ├── data.py       # Coleta os dados financeiros
│   ├── analysis.py   # Calcula retornos, estatísticas e médias móveis
│   └── charts.py     # Gera as visualizações
├── .gitignore
├── requirements.txt
└── README.md
```

## Como funciona

O fluxo atual do projeto é:

```text
yfinance
   ↓
Coleta dos dados
   ↓
Validação e preparação
   ↓
Retorno do período
   ↓
Retorno diário
   ↓
Média e volatilidade
   ↓
Médias móveis de 20 e 50 períodos
   ↓
Visualização dos preços
```

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

Execute o projeto:

```bash
python src/main.py
```

No estado atual, o ativo e o período são definidos no `src/main.py`.

## Conceitos praticados

Durante o desenvolvimento, o projeto já passou por conceitos importantes de Python e análise de dados, como:

- Funções, parâmetros e `return`
- Criação e importação de módulos próprios
- DataFrame e Series
- Indexação com `iloc`
- MultiIndex
- Criação de novas colunas
- `pct_change()`, `mean()`, `std()` e `rolling()`
- Separação de responsabilidades entre arquivos
- Visualização de séries temporais

## Roadmap

- [x] Estruturar o repositório
- [x] Configurar dependências
- [x] Coletar séries históricas com `yfinance`
- [x] Calcular retorno do período
- [x] Calcular retornos diários
- [x] Calcular média e volatilidade diária
- [x] Adicionar médias móveis de 20 e 50 períodos
- [x] Criar gráfico de preço e médias móveis
- [x] Separar coleta, análise e visualização em módulos
- [ ] Permitir seleção dinâmica de ativo e período
- [ ] Comparar diferentes ativos
- [ ] Adicionar novas visualizações
- [ ] Criar interface interativa com Streamlit
- [ ] Melhorar tratamento de erros e validações
- [ ] Documentar os resultados da análise
- [ ] Publicar uma versão final do projeto

## Status

🚧 Projeto em desenvolvimento.

A base de coleta, cálculo de indicadores e visualização já está funcionando. A próxima fase será evoluir a experiência de uso e ampliar as análises disponíveis.

## Autor

**Murillo Lourenço**  
Estudante de Análise e Desenvolvimento de Sistemas na FATEC Sorocaba.

Interesses: Dados, Inteligência Artificial, Automação e Mercado Financeiro.
