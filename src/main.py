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

def calcular_retorno(dados):
    primeiro_fechamento = dados["Close"].iloc[0]
    ultimo_fechamento = dados["Close"].iloc[-1]
    retorno = ((ultimo_fechamento - primeiro_fechamento) / primeiro_fechamento)  * 100

    return primeiro_fechamento, ultimo_fechamento, retorno

def adicionar_retorno_diario(dados):
    dados["Retorno_Diario"] = dados["Close"].pct_change() * 100

    return dados

def calcular_estatisticas(dados):
    media_retorno_diario = dados["Retorno_Diario"].mean()
    volatilidade_diaria = dados["Retorno_Diario"].std()

    return media_retorno_diario, volatilidade_diaria

ticker = "VALE3.SA"

dados = buscar_dados(ticker, "1y")
dados.columns = dados.columns.get_level_values(0)

if dados.empty:
    print("Nenhum dado foi encontrado.")
else:
    primeiro_fechamento, ultimo_fechamento, retorno = calcular_retorno(dados)
    dados = adicionar_retorno_diario(dados)
    media_retorno_diario, volatilidade_diaria = calcular_estatisticas(dados)

    print(f"\nAtivo {ticker}:")
    print(f"Primeiro fechamento: R$ {primeiro_fechamento:.2f}")
    print(f"Último fechamento: R$ {ultimo_fechamento:.2f}")
    print(f"Retorno no peródo: {retorno:.2f}%")
    print(f"Média do retorno diário: {media_retorno_diario:.2f}%")
    print(f"Total de registros: {len(dados)}")
    print(f"Volatilidade diária: {volatilidade_diaria:.2f}%")
   


    



