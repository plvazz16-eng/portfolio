import csv
from pathlib import Path

import matplotlib.pyplot as plt


SUBJECTS = [
    "linguagens",
    "humanas",
    "naturezas",
    "matematica",
    "redacao",
]


def load_data(file_path: str) -> list[dict]:
    """Carrega os dados do CSV."""

    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        return [
            {
                key: float(value) if key != "id" else int(value)
                for key, value in row.items()
            }
            for row in reader
        ]


def plot_average_scores(data: list[dict]) -> None:
    """Cria um gráfico comparando as médias das áreas."""

    averages = [
        sum(student[subject] for student in data) / len(data)
        for subject in SUBJECTS
    ]

    labels = [
        "Linguagens",
        "Humanas",
        "Naturezas",
        "Matemática",
        "Redação",
    ]

    plt.figure(figsize=(10, 6))

    plt.bar(labels, averages)

    plt.title("Média das notas por área")
    plt.xlabel("Área")
    plt.ylabel("Nota média")

    plt.ylim(0, 1000)
    plt.grid(axis="y", alpha=0.3)

    plt.tight_layout()
    plt.show()


def plot_math_distribution(data: list[dict]) -> None:
    """Cria um histograma das notas de Matemática."""

    mathematics = [
        student["matematica"]
        for student in data
    ]

    plt.figure(figsize=(10, 6))

    plt.hist(
        mathematics,
        bins=8,
        edgecolor="black",
    )

    plt.title("Distribuição das notas de Matemática")
    plt.xlabel("Nota")
    plt.ylabel("Número de participantes")

    plt.grid(axis="y", alpha=0.3)

    plt.tight_layout()
    plt.show()


def plot_math_redaction_relationship(data: list[dict]) -> None:
    """Mostra a relação entre Matemática e Redação."""

    mathematics = [
        student["matematica"]
        for student in data
    ]

    redaction = [
        student["redacao"]
        for student in data
    ]

    plt.figure(figsize=(10, 6))

    plt.scatter(
        mathematics,
        redaction,
        alpha=0.7,
    )

    plt.title("Relação entre Matemática e Redação")
    plt.xlabel("Matemática")
    plt.ylabel("Redação")

    plt.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()


def main():
    project_root = Path(__file__).resolve().parents[1]

    data_file = (
        project_root
        / "data"
        / "enem_sample.csv"
    )

    data = load_data(str(data_file))

    print("Gerando gráfico de médias...")
    plot_average_scores(data)

    print("Gerando distribuição de Matemática...")
    plot_math_distribution(data)

    print("Gerando relação Matemática x Redação...")
    plot_math_redaction_relationship(data)


if __name__ == "__main__":
    main()