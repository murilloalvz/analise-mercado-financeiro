import matplotlib.pyplot as plt

def plotar_precos(dados, ticker):
    plt.figure(figsize=(12, 6))

    plt.plot(dados.index, dados["Close"], label="Fechamento")
    plt.plot(dados.index, dados["Media_Movel_20"], label="Média Móvel 20")
    plt.plot(dados.index, dados["Media_Movel_50"], label="Média Móvel 50")

    plt.title(f"Histórico de preços -- {ticker}")
    plt.xlabel("Data")
    plt.ylabel("Preço")
    plt.legend()

    fig = plt.gcf()

    return fig

def plotar_comparacao(dados, dados_comparacao, ticker, ticker_comparacao):
    plt.figure(figsize=(12, 6))
    
    plt.plot(dados.index, dados["Preco_Normalizado"], label= f"Fechamento: {ticker}")
    plt.plot(dados_comparacao.index, dados_comparacao["Preco_Normalizado"], label= f"Fechamento: {ticker_comparacao}")
    
    plt.title(f"Comparação De Desempenho -- {ticker} x {ticker_comparacao}")
    plt.xlabel("Data")
    plt.ylabel("Desempenho normalizado (base 100)")
    plt.legend()
    
    fig_comparacao = plt.gcf()
    
    return fig_comparacao