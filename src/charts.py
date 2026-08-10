import matplotlib.pyplot as plt

def plotar_precos(dados, ticker):
    plt.figure(figsize=(12, 6))

    plt.plot(dados.index, dados["Close"], label="Fechamento")
    plt.plot(dados.index, dados["Media_Movel_20"], label="Média Móvel 20")
    plt.plot(dados.index, dados["Media_Movel_50"], label="Média Móvel 50")

    plt.title(f"Histórico de preços -- {ticker}")
    plt.xlabel("Data")
    plt.ylabel("Preço (R$)")
    plt.legend()

    fig = plt.gcf()

    return fig