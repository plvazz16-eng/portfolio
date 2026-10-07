import sys
from pathlib import Path

import matplotlib.pyplot as plt
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


INITIAL_CAPITAL = 10_000.00

SIGNAL_THRESHOLD = 0.55


def calculate_max_drawdown(
    equity_curve: pd.Series,
) -> float:

    running_max = (
        equity_curve.cummax()
    )

    drawdown = (
        equity_curve
        / running_max
        - 1
    )

    return drawdown.min()


def calculate_sharpe_ratio(
    returns: pd.Series,
) -> float:

    if returns.std() == 0:
        return 0.0

    return (
        returns.mean()
        / returns.std()
    ) * (
        252 ** 0.5
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

    # ==========================================
    # FEATURES
    # ==========================================

    df = calculate_features(
        df
    )

    df = create_target(
        df
    )

    X, y = prepare_dataset(
        df
    )

    # ==========================================
    # TRAIN / TEST
    # ==========================================

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

    # ==========================================
    # TRAIN MODEL
    # ==========================================

    model = train_model(
        X_train,
        y_train,
    )

    probabilities = (
        model.predict_proba(
            X_test
        )[:, 1]
    )

    # ==========================================
    # TEST DATA
    # ==========================================

    results = df.loc[
        X_test.index
    ].copy()

    results["probability"] = (
        probabilities
    )

    # Sinal da estratégia.
    #
    # 1 = investido
    # 0 = caixa
    results["signal"] = (
        results["probability"]
        >= SIGNAL_THRESHOLD
    ).astype(int)

    # ==========================================
    # RETORNOS
    # ==========================================

    results["market_return"] = (
        results["close"].pct_change()
    )

    # Estratégia ML:
    # utiliza o sinal do dia anterior.
    results["strategy_return"] = (
        results["signal"].shift(1)
        * results["market_return"]
    )

    results["strategy_return"] = (
        results["strategy_return"]
        .fillna(0)
    )

    results["market_return"] = (
        results["market_return"]
        .fillna(0)
    )

    # ==========================================
    # EQUITY CURVES
    # ==========================================

    results["ml_equity"] = (
        INITIAL_CAPITAL
        * (
            1
            + results["strategy_return"]
        ).cumprod()
    )

    results["buy_hold_equity"] = (
        INITIAL_CAPITAL
        * (
            1
            + results["market_return"]
        ).cumprod()
    )

    # ==========================================
    # MÉTRICAS
    # ==========================================

    ml_return = (
        results["ml_equity"].iloc[-1]
        / INITIAL_CAPITAL
        - 1
    )

    buy_hold_return = (
        results["buy_hold_equity"].iloc[-1]
        / INITIAL_CAPITAL
        - 1
    )

    ml_drawdown = (
        calculate_max_drawdown(
            results["ml_equity"]
        )
    )

    buy_hold_drawdown = (
        calculate_max_drawdown(
            results["buy_hold_equity"]
        )
    )

    ml_sharpe = (
        calculate_sharpe_ratio(
            results["strategy_return"]
        )
    )

    buy_hold_sharpe = (
        calculate_sharpe_ratio(
            results["market_return"]
        )
    )

    invested_percentage = (
        results["signal"].mean()
    )

    operations = (
        results["signal"]
        .diff()
        .abs()
        .sum()
        / 2
    )

    # ==========================================
    # RESULTADOS
    # ==========================================

    print(
        "\n" + "=" * 65
    )

    print(
        "BACKTEST RESULTS"
    )

    print(
        "=" * 65
    )

    print(
        f"\nInitial capital: "
        f"${INITIAL_CAPITAL:,.2f}"
    )

    print(
        "\nMachine Learning Strategy"
    )

    print(
        f"Final value: "
        f"${results['ml_equity'].iloc[-1]:,.2f}"
    )

    print(
        f"Return: "
        f"{ml_return:.2%}"
    )

    print(
        f"Max drawdown: "
        f"{ml_drawdown:.2%}"
    )

    print(
        f"Sharpe ratio: "
        f"{ml_sharpe:.2f}"
    )

    print(
        f"Time invested: "
        f"{invested_percentage:.2%}"
    )

    print(
        f"Operations: "
        f"{operations:.0f}"
    )

    print(
        "\nBuy & Hold"
    )

    print(
        f"Final value: "
        f"${results['buy_hold_equity'].iloc[-1]:,.2f}"
    )

    print(
        f"Return: "
        f"{buy_hold_return:.2%}"
    )

    print(
        f"Max drawdown: "
        f"{buy_hold_drawdown:.2%}"
    )

    print(
        f"Sharpe ratio: "
        f"{buy_hold_sharpe:.2f}"
    )

    print(
        "\n" + "=" * 65
    )

    # ==========================================
    # GRÁFICO
    # ==========================================

    plt.figure(
        figsize=(11, 6)
    )

    plt.plot(
        results["date"],
        results["ml_equity"],
        linewidth=2,
        label="ML Strategy",
    )

    plt.plot(
        results["date"],
        results["buy_hold_equity"],
        linewidth=2,
        label="Buy & Hold",
    )

    plt.title(
        "Machine Learning Strategy vs Buy & Hold"
    )

    plt.xlabel(
        "Date"
    )

    plt.ylabel(
        "Portfolio Value ($)"
    )

    plt.xticks(
        rotation=45
    )

    plt.grid(
        True,
        alpha=0.3,
    )

    plt.legend()

    plt.tight_layout()

    plt.show()


if __name__ == "__main__":
    main()