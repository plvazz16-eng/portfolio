import csv
import math
import random
from datetime import date, timedelta


random.seed(42)


NUMBER_OF_DAYS = 500
INITIAL_PRICE = 100.0


def generate_market_data():
    rows = []

    current_date = date(2024, 1, 2)
    price = INITIAL_PRICE

    trading_day = 0

    while len(rows) < NUMBER_OF_DAYS:

        cycle = trading_day % 120

        # ==========================================
        # REGIMES DE MERCADO
        # ==========================================

        if cycle < 40:
            # Tendência de alta
            drift = 0.0020
            volatility = 0.009

        elif cycle < 80:
            # Mercado lateral
            drift = 0.0000
            volatility = 0.012

        else:
            # Tendência de baixa
            drift = -0.0020
            volatility = 0.009

        # ==========================================
        # COMPONENTE CÍCLICA
        # ==========================================

        cyclical_component = (
            math.sin(trading_day / 10)
            * 0.0015
        )

        # ==========================================
        # RUÍDO
        # ==========================================

        random_component = random.gauss(
            0,
            volatility,
        )

        daily_return = (
            drift
            + cyclical_component
            + random_component
        )

        previous_close = price

        price *= (
            1 + daily_return
        )

        # Evita preços irrealistas.
        price = max(
            price,
            20,
        )

        # ==========================================
        # OHLC
        # ==========================================

        open_price = (
            previous_close
            * (
                1
                + random.gauss(
                    0,
                    0.003,
                )
            )
        )

        daily_range = abs(
            random.gauss(
                volatility * 1.5,
                volatility * 0.4,
            )
        )

        high_price = (
            max(
                open_price,
                price,
            )
            * (
                1 + daily_range
            )
        )

        low_price = (
            min(
                open_price,
                price,
            )
            * (
                1 - daily_range
            )
        )

        # ==========================================
        # VOLUME
        # ==========================================

        base_volume = 2_000_000

        volume_multiplier = (
            1
            + abs(daily_return) * 20
        )

        volume = int(
            base_volume
            * volume_multiplier
            * random.uniform(
                0.85,
                1.15,
            )
        )

        rows.append(
            {
                "date": current_date.isoformat(),
                "open": round(
                    open_price,
                    2,
                ),
                "high": round(
                    high_price,
                    2,
                ),
                "low": round(
                    low_price,
                    2,
                ),
                "close": round(
                    price,
                    2,
                ),
                "volume": volume,
            }
        )

        current_date += timedelta(
            days=1
        )

        # Pula fins de semana.
        while current_date.weekday() >= 5:
            current_date += timedelta(
                days=1
            )

        trading_day += 1

    return rows


def save_data(rows):
    output_file = (
        "machine-learning/data/"
        "market_data.csv"
    )

    with open(
        output_file,
        "w",
        newline="",
        encoding="utf-8",
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=[
                "date",
                "open",
                "high",
                "low",
                "close",
                "volume",
            ],
        )

        writer.writeheader()
        writer.writerows(rows)


def main():

    rows = generate_market_data()

    save_data(rows)

    print(
        f"Dataset criado com "
        f"{len(rows)} pregões."
    )


if __name__ == "__main__":
    main()