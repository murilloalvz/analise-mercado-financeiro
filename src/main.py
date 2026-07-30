import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

ticker = "PETR4.SA"

dados = yf.download(
    ticker,
    period="1y",
    auto_adjust=True,
    progress=False,
)

if dados.empty:
    print("Nenhum dado foi encontrado.")
else:
    print(f"Dados encontrados para {ticker}:")
    print(dados.head())
    print(f"\nTotal de registros: {len(dados)}")