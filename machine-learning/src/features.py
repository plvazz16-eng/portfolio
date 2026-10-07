import pandas as pd


def calculate_features(
    df: pd.DataFrame,
) -> pd.DataFrame:
    """
    Cria indicadores utilizados pelo modelo
    de Machine Learning.
    """

    data = df.copy()

    # ==========================================
    # RETORNOS
    # ==========================================

    data["daily_return"] = (
        data["close"].pct_change()
    )

    data["return_5d"] = (
        data["close"].pct_change(5)
    )

    data["return_10d"] = (
        data["close"].pct_change(10)
    )

    # ==========================================
    # MÉDIAS MÓVEIS
    # ==========================================

    data["ma_5"] = (
        data["close"]
        .rolling(window=5)
        .mean()
    )

    data["ma_10"] = (
        data["close"]
        .rolling(window=10)
        .mean()
    )

    # Distância do preço para MA5
    data["price_to_ma5"] = (
        data["close"] / data["ma_5"] - 1
    )

    # Distância do preço para MA10
    data["price_to_ma10"] = (
        data["close"] / data["ma_10"] - 1
    )

    # Relação entre médias móveis
    data["ma_ratio"] = (
        data["ma_5"] / data["ma_10"] - 1
    )

    # ==========================================
    # MOMENTUM
    # ==========================================

    data["momentum_5d"] = (
        data["close"]
        - data["close"].shift(5)
    )

    data["momentum_10d"] = (
        data["close"]
        - data["close"].shift(10)
    )

    # ==========================================
    # VOLATILIDADE
    # ==========================================

    data["volatility_5d"] = (
        data["daily_return"]
        .rolling(window=5)
        .std()
    )

    data["volatility_10d"] = (
        data["daily_return"]
        .rolling(window=10)
        .std()
    )

    # ==========================================
    # PRICE ACTION
    # ==========================================

    # Tamanho relativo do candle
    data["daily_range"] = (
        (data["high"] - data["low"])
        / data["close"]
    )

    # Posição do fechamento dentro do range
    data["close_position"] = (
        (data["close"] - data["low"])
        / (data["high"] - data["low"])
    )

    # ==========================================
    # VOLUME
    # ==========================================

    data["volume_change"] = (
        data["volume"].pct_change()
    )

    data["volume_ma_5"] = (
        data["volume"]
        .rolling(window=5)
        .mean()
    )

    data["volume_ratio"] = (
        data["volume"]
        / data["volume_ma_5"]
    )

    return data


def create_target(
    df: pd.DataFrame,
    horizon: int = 5,
) -> pd.DataFrame:
    """
    Cria o alvo do modelo.

    Target:

    1 → retorno positivo nos próximos 5 dias
    0 → retorno negativo ou zero
    """

    data = df.copy()

    future_return = (
        data["close"].shift(-horizon)
        / data["close"]
        - 1
    )

    # Remove registros sem informação futura.
    data = data.loc[
        future_return.notna()
    ].copy()

    data["future_return"] = (
        future_return.loc[data.index]
    )

    data["target"] = (
        data["future_return"] > 0
    ).astype(int)

    return data