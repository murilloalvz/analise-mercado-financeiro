import streamlit as st
from src.data import buscar_dados
from src.analysis import (
    calcular_retorno,
    adicionar_retorno_diario,
    calcular_estatisticas,
    adicionar_medias_moveis,
    adicionar_preco_normalizado,
)
from src.charts import (
    plotar_precos,
    plotar_comparacao,
)

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

    ticker_comparacao = st.text_input(
            "Digite o ticker do ativo para comparação (ex: VALE3.SA):", 
            "VALE3.SA"
        )
                       
    periodo = st.selectbox(
        "Selecione o período de análise:", 
        ["1mo", "3mo", "6mo", "1y", "2y", "5y"]
    )

dados = buscar_dados(ticker, periodo)
dados_comparacao = buscar_dados(ticker_comparacao, periodo)

if dados.empty or dados_comparacao.empty: 
    st.error("Nenhum dado foi encontrado para um dos ativos informados.")
else:
    dados.columns = dados.columns.get_level_values(0)
    dados_comparacao.columns = dados_comparacao.columns.get_level_values(0)

    primeiro_fechamento, ultimo_fechamento, retorno = calcular_retorno(dados)
    dados = adicionar_retorno_diario(dados)
    dados_comparacao = adicionar_retorno_diario(dados_comparacao)
    dados = adicionar_medias_moveis(dados)
    dados = adicionar_preco_normalizado(dados)
    dados_comparacao =  adicionar_preco_normalizado(dados_comparacao)
    media_retorno_diario, volatilidade_diaria = calcular_estatisticas(dados) 
    media_retorno_diario_comparacao, volatilidade_diaria_comparacao = calcular_estatisticas(dados_comparacao)
    fig = plotar_precos(dados, ticker)   
    fig_comparacao = plotar_comparacao(dados, dados_comparacao, ticker, ticker_comparacao)

    primeiro_fechamento_comparacao, ultimo_fechamento_comparacao, retorno_comparacao = calcular_retorno(dados_comparacao)

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
    st.subheader(f"Evolução do preço - {ticker}")
    st.pyplot(fig)

    st.divider()
    st.subheader("Comparação de Ativos")

    col4, col5= st.columns(2)

    with col4:
        st.subheader(f"{ticker}")
        st.metric(label="Retorno:", value=f"{retorno:.2f}%")
        st.metric(label="Volatilidade:", value=f"{volatilidade_diaria:.4f}%")

    with col5:
        st.subheader(f"{ticker_comparacao}")
        st.metric(label="Retorno:", value=f"{retorno_comparacao:.2f}%")
        st.metric(label="Volatilidade:", value=f"{volatilidade_diaria_comparacao:.4f}%")
        
    st.pyplot(fig_comparacao)

