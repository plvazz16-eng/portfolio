import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
)


FEATURES = [
    "daily_return",
    "return_5d",
    "return_10d",
    "ma_5",
    "ma_10",
    "price_to_ma5",
    "price_to_ma10",
    "ma_ratio",
    "momentum_5d",
    "momentum_10d",
    "volatility_5d",
    "volatility_10d",
    "daily_range",
    "close_position",
    "volume_change",
    "volume_ratio",
]


def prepare_dataset(
    df: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.Series]:

    data = df.copy()

    data = data.dropna(
        subset=FEATURES + ["target"]
    )

    X = data[FEATURES]
    y = data["target"]

    return X, y


def show_feature_importance(
    model: RandomForestClassifier,
) -> None:

    importance = pd.Series(
        model.feature_importances_,
        index=FEATURES,
    ).sort_values(
        ascending=False
    )

    print("\nFeature Importance:")
    print("-" * 50)

    for feature, value in importance.items():
        print(
            f"{feature:<22} {value:.4f}"
        )


def train_model(
    X_train: pd.DataFrame,
    y_train: pd.Series,
) -> RandomForestClassifier:

    model = RandomForestClassifier(
        n_estimators=300,
        max_depth=7,
        min_samples_leaf=5,
        random_state=42,
        class_weight="balanced",
    )

    model.fit(
        X_train,
        y_train,
    )

    return model


def evaluate_model(
    model: RandomForestClassifier,
    X_test: pd.DataFrame,
    y_test: pd.Series,
) -> None:

    predictions = model.predict(
        X_test
    )

    accuracy = accuracy_score(
        y_test,
        predictions,
    )

    print("\n" + "=" * 60)
    print("MODEL EVALUATION")
    print("=" * 60)

    print(
        f"\nAccuracy: {accuracy:.2%}"
    )

    print("\nClassification Report:")

    print(
        classification_report(
            y_test,
            predictions,
            target_names=[
                "Negative",
                "Positive",
            ],
        )
    )

    print("Confusion Matrix:")

    matrix = confusion_matrix(
        y_test,
        predictions,
    )

    print(matrix)