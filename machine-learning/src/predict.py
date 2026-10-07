import sys
from pathlib import Path

import pandas as pd


sys.path.insert(
    0,
    str(Path(__file__).resolve().parent),
)


from features import (
    calculate_features,
    create_target,
)

from model import (
    prepare_dataset,
    train_model,
)


def main():

    project_root = (
        Path(__file__).resolve().parents[1]
    )

    data_file = (
        project_root
        / "data"
        / "market_data.csv"
    )

    df = pd.read_csv(
        data_file
    )

    # Cria as features.
    df = calculate_features(
        df
    )

    # Cria o target.
    df = create_target(
        df
    )

    # Remove linhas que não possuem
    # todas as features necessárias.
    X, y = prepare_dataset(
        df
    )

    # Mantém a ordem temporal:
    # passado → treinamento
    # futuro → teste
    split_index = int(
        len(X) * 0.8
    )

    X_train = X.iloc[
        :split_index
    ]

    X_test = X.iloc[
        split_index:
    ]

    y_train = y.iloc[
        :split_index
    ]

    # Treina somente utilizando
    # os dados históricos.
    model = train_model(
        X_train,
        y_train,
    )

    # Probabilidade de retorno positivo.
    probabilities = (
        model.predict_proba(
            X_test
        )[:, 1]
    )

    # Recupera exatamente os mesmos
    # índices utilizados em X_test.
    results = df.loc[
        X_test.index
    ].copy()

    results["probability"] = (
        probabilities
    )

    results["prediction"] = (
        results["probability"] >= 0.50
    ).astype(int)

    print(
        "=" * 65
    )

    print(
        "ML MARKET SIGNALS"
    )

    print(
        "=" * 65
    )

    print(
        f"\nTraining samples: "
        f"{len(X_train)}"
    )

    print(
        f"Testing samples: "
        f"{len(X_test)}"
    )

    print(
        "\nÚltimos sinais:"
    )

    print(
        "-" * 65
    )

    for _, row in results.tail(
        10
    ).iterrows():

        if row["probability"] >= 0.50:
            signal = "LONG"
        else:
            signal = "CASH"

        print(
            f"{row['date']} | "
            f"Close: {row['close']:>8.2f} | "
            f"Prob. alta: "
            f"{row['probability']:.2%} | "
            f"Sinal: {signal}"
        )


if __name__ == "__main__":
    main()