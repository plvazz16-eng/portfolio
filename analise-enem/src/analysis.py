import csv
from pathlib import Path

from stats import (
    calculate_correlation,
    calculate_mean,
    calculate_median,
    calculate_standard_deviation,
)


SUBJECTS = [
    "linguagens",
    "humanas",
    "naturezas",
    "matematica",
    "redacao",
]


def load_data(file_path: str) -> list[dict]:
    """Carrega os dados do arquivo CSV."""

    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        return [
            {
                key: float(value) if key != "id" else int(value)
                for key, value in row.items()
            }
            for row in reader
        ]


def analyze_subjects(data: list[dict]) -> None:
    """Exibe estatísticas descritivas das áreas."""

    print("\n" + "=" * 65)
    print("ANÁLISE ESTATÍSTICA DO ENEM")
    print("=" * 65)

    print(
        f"{'Área':<15}"
        f"{'Média':>12}"
        f"{'Mediana':>12}"
        f"{'Desvio P.':>14}"
    )

    print("-" * 65)

    for subject in SUBJECTS:
        values = [student[subject] for student in data]

        average = calculate_mean(values)
        med = calculate_median(values)
        deviation = calculate_standard_deviation(values)

        print(
            f"{subject.capitalize():<15}"
            f"{average:>12.2f}"
            f"{med:>12.2f}"
            f"{deviation:>14.2f}"
        )


def analyze_correlations(data: list[dict]) -> None:
    """Analisa a correlação entre Matemática e outras áreas."""

    mathematics = [
        student["matematica"]
        for student in data
    ]

    print("\n" + "=" * 65)
    print("CORRELAÇÃO COM MATEMÁTICA")
    print("=" * 65)

    correlations = []

    for subject in SUBJECTS:
        if subject == "matematica":
            continue

        values = [
            student[subject]
            for student in data
        ]

        correlation = calculate_correlation(
            mathematics,
            values,
        )

        correlations.append(
            (subject, correlation)
        )

    correlations.sort(
        key=lambda item: item[1],
        reverse=True,
    )

    for subject, correlation in correlations:
        print(
            f"{subject.capitalize():<15}"
            f"{correlation:.3f}"
        )

    strongest = correlations[0]

    print("\nMaior correlação com Matemática:")
    print(
        f"{strongest[0].capitalize()} "
        f"({strongest[1]:.3f})"
    )


def main():
    project_root = Path(__file__).resolve().parents[1]

    data_file = (
        project_root
        / "data"
        / "enem_sample.csv"
    )

    data = load_data(str(data_file))

    print(f"\nParticipantes analisados: {len(data)}")

    analyze_subjects(data)
    analyze_correlations(data)


if __name__ == "__main__":
    main()