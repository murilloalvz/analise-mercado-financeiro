import yfinance as yf


def buscar_dados(ticker, periodo):
    dados = yf.download(
        ticker,
        period=periodo,
        auto_adjust=True,
        progress=False,
    )

    if not dados.empty:
         dados.columns = dados.columns.get_level_values(0)
    
    return dados
