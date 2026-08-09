import streamlit as st
from src.data import buscar_dados
from src.analysis import (
    calcular_retorno,
    adicionar_retorno_diario,
    calcular_estatisticas,
    adicionar_medias_moveis,
)

st.title ("Análise de Mercado Financeiro")

ticker = st.text_input(
    "Digite o ticker do ativo (ex: PETR4.SA):", 
    "PETR4.SA"
    )

periodo = st.selectbox(
    "Selecione o período de análise:", 
    ["1mo", "3mo", "6mo", "1y", "2y", "5y"]
    )

dados = buscar_dados(ticker, periodo)
dados.columns = dados.columns.get_level_values(0)

if dados.empty: 
    st.error("Nenhum dado foi encontrado para o ticker informado.")
else:
    primeiro_fechamento, ultimo_fechamento, retorno = calcular_retorno(dados)
    dados = adicionar_retorno_diario(dados)
    dados = adicionar_medias_moveis(dados)
    media_retorno_diario, volatilidade_diaria = calcular_estatisticas(dados)    

    st.metric(label="Retorno no período", value=f"{retorno:.2f}%")
    st.metric(label="Média do Retorno Diário", value=f"{media_retorno_diario:.4f}%")
    st.metric(label="Volatilidade Diária", value=f"{volatilidade_diaria:.4f}%")
   