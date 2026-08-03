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

dados = buscar_dados(ticker, "6mo")

if dados.empty:
    print("Nenhum dado foi encontrado.")
else:
    print(f"Dados encontrados para {ticker}:")
    print(dados.head())
    print(f"\nTotal de registros: {len(dados)}")

