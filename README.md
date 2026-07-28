# Análise do Mercado Financeiro

Projeto em desenvolvimento para coletar, tratar e analisar dados reais do mercado financeiro com Python.

A proposta é construir um fluxo completo de análise: obtenção dos dados, limpeza, cálculo de indicadores e criação de visualizações que apoiem a comparação entre ativos.

## Objetivos

- Consumir dados financeiros por meio da biblioteca `yfinance`
- Organizar séries históricas com Pandas
- Calcular métricas e retornos
- Comparar o comportamento de diferentes ativos
- Criar visualizações claras com Matplotlib
- Aplicar boas práticas de organização e versionamento

## Tecnologias

- Python
- Pandas
- NumPy
- yfinance
- Matplotlib
- Git e GitHub

## Estrutura planejada

```text
analise-mercado-financeiro/
├── data/
├── images/
├── src/
├── .gitignore
├── requirements.txt
└── README.md
```

## Como executar

```bash
git clone https://github.com/murilloalvz/analise-mercado-financeiro.git
cd analise-mercado-financeiro
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

## Roadmap

- [x] Estruturar o repositório
- [x] Configurar dependências
- [ ] Definir os ativos analisados
- [ ] Coletar séries históricas
- [ ] Tratar valores ausentes
- [ ] Calcular retornos e volatilidade
- [ ] Comparar ativos
- [ ] Criar gráficos
- [ ] Documentar resultados
- [ ] Publicar uma versão final da análise

## Status

🚧 Projeto em desenvolvimento.

## Autor

**Murillo Lourenço**  
Estudante de Análise e Desenvolvimento de Sistemas na FATEC Sorocaba.

Interesses: Dados, Inteligência Artificial, Automação e Mercado Financeiro.