import sys
from pathlib import Path

import pandas as pd


sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[1] / "src"),
)


from features import (
    calculate_features,
    create_target,
)

from model import (
    prepare_dataset,
    train_model,
)


def create_sample_data() -> pd.DataFrame:
    """Cria um pequeno dataset para os testes."""

    rows = []

    price = 100.0

    for day in range(30):

        price *= 1 + (
            0.002 if day % 2 == 0 else -0.001
        )

        rows.append(
            {
                "date": f"2024-01-{day + 1:02d}",
                "open": price,
                "high": price * 1.01,
                "low": price * 0.99,
                "close": price,
                "volume": 1_000_000 + day * 10_000,
            }
        )

    return pd.DataFrame(rows)


def test_features_are_created():
    """Verifica se os indicadores são calculados."""

    df = create_sample_data()

    result = calculate_features(df)

    expected_columns = [
        "daily_return",
        "return_5d",
        "return_10d",
        "ma_5",
        "ma_10",
        "volatility_5d",
        "volatility_10d",
        "volume_ratio",
    ]

    for column in expected_columns:
        assert column in result.columns


def test_target_is_created():
    """Verifica se o target possui valores válidos."""

    df = create_sample_data()

    df = calculate_features(df)

    result = create_target(df)

    assert "future_return" in result.columns
    assert "target" in result.columns

    assert set(
        result["target"].unique()
    ).issubset({0, 1})


def test_target_removes_future_unknown_rows():
    """Verifica se os últimos dias sem futuro são removidos."""

    df = create_sample_data()

    df = calculate_features(df)

    result = create_target(
        df,
        horizon=5,
    )

    assert len(result) == 25


def test_prepare_dataset():
    """Verifica a preparação de X e y."""

    df = create_sample_data()

    df = calculate_features(df)

    df = create_target(df)

    X, y = prepare_dataset(df)

    assert len(X) == len(y)
    assert len(X) > 0


def test_model_can_train():
    """Verifica se o Random Forest consegue ser treinado."""

    df = create_sample_data()

    df = calculate_features(df)

    df = create_target(df)

    X, y = prepare_dataset(df)

    model = train_model(
        X,
        y,
    )

    predictions = model.predict(X)

    assert len(predictions) == len(y)
    assert set(
        predictions
    ).issubset({0, 1})


if __name__ == "__main__":
    test_features_are_created()
    test_target_is_created()
    test_target_removes_future_unknown_rows()
    test_prepare_dataset()
    test_model_can_train()

    print(
        "\nAll Machine Learning tests passed!"
    )