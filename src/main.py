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

if dados.empty:
    print("Nenhum dado foi encontrado.")
else:
    print(f"Dados encontrados para {ticker}:")
    print(dados.head())

    ultimo_fechamento = dados["Close"].iloc[-1].iloc[0]

    print(f"\nÚltimo fechamento: R$ {ultimo_fechamento:.2f}")
    print(f"\nTotal de registros: {len(dados)}")



