import streamlit as st
from src.data import buscar_dados
from src.analysis import (
    calcular_retorno,
    adicionar_retorno_diario,
    calcular_estatisticas,
    adicionar_medias_moveis,
)
from src.charts import plotar_precos

st.set_page_config(
    page_title="Análise de Mercado Financeiro",
    page_icon="📈",
    layout="wide",
)

st.title ("Análise de Mercado Financeiro")

with st.sidebar:
    st.subheader("Filtros")
    
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
    fig = plotar_precos(dados, ticker)   

    with st.sidebar:
        st.divider()
        st.subheader("Estatísticas")
        st.metric("Total de registros", dados.shape[0])
        st.metric("Preço inicial:", value=f"R$ {primeiro_fechamento:.2f}")
        st.metric("Preço atual:", value=f"R$ {ultimo_fechamento:.2f}", delta=f" {retorno:.2f}%")
        
        if dados.shape[0] < 50:
            st.warning("Pode não haver dados suficientes para visualizar a média móvel de 50 períodos!")

    st.divider()
    st.subheader("Resumo do ativo")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(label="Retorno no período", value=f"{retorno:.2f}%")

    with col2:
        st.metric(label="Média do Retorno Diário", value=f"{media_retorno_diario:.4f}%")

    with col3:
        st.metric(label="Volatilidade Diária", value=f"{volatilidade_diaria:.4f}%")

    st.divider()
    st.subheader("Evolução do preço")

    st.pyplot(fig)

