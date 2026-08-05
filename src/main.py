import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

def buscar_dados(ticker, periodo):
    dados = yf.download(
        ticker,
        period=periodo,
        auto_adjust=True,
        progress=False,
)

    return dados

ticker = "VALE3.SA"

dados = buscar_dados(ticker, "1y")
dados.columns = dados.columns.get_level_values(0)

if dados.empty:
    print("Nenhum dado foi encontrado.")
else:
    print(f"Dados encontrados para {ticker}:")
    print(dados.head())

    primeiro_fechamento = dados["Close"].iloc[0]
    ultimo_fechamento = dados["Close"].iloc[-1]
    retorno = ((ultimo_fechamento - primeiro_fechamento) / primeiro_fechamento)  * 100
    dados["Retorno_Diario"] = dados["Close"].pct_change() * 100
    media_retorno_diario = dados["Retorno_Diario"].mean()
    volatilidade_diaria = dados["Retorno_Diario"].std()

    print(f"\nPrimeiro fechamento: R$ {primeiro_fechamento:.2f}")
    print(f"Último fechamento: R$ {ultimo_fechamento:.2f}")
    print(f"Retorno no peródo: {retorno:.2f}%")
    print(f"Média do retorno diário: {media_retorno_diario:.2f}%")
    print(f"Total de registros: {len(dados)}")
    print(f"Volatilidade diária: {volatilidade_diaria:.2f}%")
    print(dados[["Close", "Retorno_Diario"]].tail())


    



