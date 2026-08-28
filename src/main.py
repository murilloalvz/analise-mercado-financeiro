import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from data import buscar_dados
from analysis import (
    calcular_retorno,
    adicionar_retorno_diario,
    calcular_estatisticas,
    adicionar_medias_moveis,
)
from charts import plotar_precos

ticker = "PETR4.SA"
periodo = "1y"

dados = buscar_dados(ticker, periodo)
dados.columns = dados.columns.get_level_values(0)

if dados.empty:
    print("Nenhum dado foi encontrado.")
else:
    primeiro_fechamento, ultimo_fechamento, retorno = calcular_retorno(dados)
    dados = adicionar_retorno_diario(dados)
    dados = adicionar_medias_moveis(dados)
    media_retorno_diario, volatilidade_diaria = calcular_estatisticas(dados)

    print(f"\nAtivo: {ticker}")
    print(f"Primeiro fechamento: R$ {primeiro_fechamento:.2f}")
    print(f"Último fechamento: R$ {ultimo_fechamento:.2f}")
    print(f"Retorno no peródo: {retorno:.2f}%")
    print(f"Média do retorno diário: {media_retorno_diario:.2f}%")
    print(f"Total de registros: {len(dados)}")
    print(f"Volatilidade diária: {volatilidade_diaria:.2f}%")

    plotar_precos(dados, ticker)
