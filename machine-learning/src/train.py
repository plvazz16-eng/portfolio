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
    evaluate_model,
    show_feature_importance,
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

    df = calculate_features(
        df
    )

    df = create_target(
        df
    )

    X, y = prepare_dataset(
        df
    )

    # 80% dos dados mais antigos
    # para treinamento.
    # 20% dos dados mais recentes
    # para teste.
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

    y_test = y.iloc[
        split_index:
    ]

    print(
        "=" * 60
    )

    print(
        "INVESTMENT PREDICTOR"
    )

    print(
        "=" * 60
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
        "\nTraining model..."
    )

    model = train_model(
        X_train,
        y_train,
    )

    evaluate_model(
        model,
        X_test,
        y_test,
    )

    show_feature_importance(
        model
    )


if __name__ == "__main__":
    main()