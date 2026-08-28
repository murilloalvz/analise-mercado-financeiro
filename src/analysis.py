def calcular_retorno(dados):
    primeiro_fechamento = dados["Close"].iloc[0]
    ultimo_fechamento = dados["Close"].iloc[-1]
    retorno = ((ultimo_fechamento - primeiro_fechamento) / primeiro_fechamento) * 100

    return primeiro_fechamento, ultimo_fechamento, retorno


def adicionar_retorno_diario(dados):
    dados = dados.copy()
    dados["Retorno_Diario"] = dados["Close"].pct_change() * 100

    return dados


def calcular_estatisticas(dados):
    media_retorno_diario = dados["Retorno_Diario"].mean()
    volatilidade_diaria = dados["Retorno_Diario"].std()

    return media_retorno_diario, volatilidade_diaria


def adicionar_medias_moveis(dados):
    dados = dados.copy()
    dados["Media_Movel_20"] = dados["Close"].rolling(window=20).mean()
    dados["Media_Movel_50"] = dados["Close"].rolling(window=50).mean()

    return dados


def adicionar_preco_normalizado(dados):
    dados = dados.copy()
    dados["Preco_Normalizado"] = (dados["Close"] / dados["Close"].iloc[0]) * 100

    return dados


def desempenho_relativo(retorno, retorno_comparacao):
    return retorno - retorno_comparacao
