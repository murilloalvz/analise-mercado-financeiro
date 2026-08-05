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

ticker = "PETR4.SA"

dados = buscar_dados(ticker, "1y")

if dados.empty:
    print("Nenhum dado foi encontrado.")
else:
    print(f"Dados encontrados para {ticker}:")
    print(dados.head())

    primeiro_fechamento = dados["Close"].iloc[0].iloc[0]
    ultimo_fechamento = dados["Close"].iloc[-1].iloc[0]
    retorno = ((ultimo_fechamento - primeiro_fechamento) / primeiro_fechamento)  * 100

    print(f"\nPrimeiro fechamento: R$ {primeiro_fechamento:.2f}")
    print(f"Último fechamento: R$ {ultimo_fechamento:.2f}")
    print(f"Retorno no peródo: {retorno:.2f}%")
    print(f"Total de registros: {len(dados)}")



