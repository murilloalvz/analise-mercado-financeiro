import matplotlib.pyplot as plt


def plotar_precos(dados, ticker):
    fig, ax = plt.subplots(figsize=(12, 6))

    ax.plot(dados.index, dados["Close"], label="Fechamento")
    ax.plot(dados.index, dados["Media_Movel_20"], label="Média Móvel 20")
    ax.plot(dados.index, dados["Media_Movel_50"], label="Média Móvel 50")

    ax.set_title(f"Histórico de preços -- {ticker}")
    ax.set_xlabel("Data")
    ax.set_ylabel("Preço")
    ax.legend()

    return fig


def plotar_comparacao(dados, dados_comparacao, ticker, ticker_comparacao):
    fig_comparacao, ax = plt.subplots(figsize=(12, 6))

    ax.plot(dados.index, dados["Preco_Normalizado"], label=f"Fechamento: {ticker}")
    ax.plot(
        dados_comparacao.index,
        dados_comparacao["Preco_Normalizado"],
        label=f"Fechamento: {ticker_comparacao}",
    )

    ax.set_title(f"Comparação De Desempenho -- {ticker} x {ticker_comparacao}")
    ax.set_xlabel("Data")
    ax.set_ylabel("Desempenho normalizado (base 100)")
    ax.legend()

    return fig_comparacao
