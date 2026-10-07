from statistics import mean, median, stdev

def calculate_mean(values: list[float]) -> float:
    """Calcula a média aritmética."""
    return mean(values)


def calculate_median(values: list[float]) -> float:
    """Calcula a mediana."""
    return median(values)


def calculate_standard_deviation(values: list[float]) -> float:
    """Calcula o desvio padrão."""
    if len(values) < 2:
        return 0.0

    return stdev(values)


def calculate_correlation(
    x_values: list[float],
    y_values: list[float],
) -> float:
    """Calcula a correlação de Pearson entre duas variáveis."""

    if len(x_values) != len(y_values):
        raise ValueError("As listas devem possuir o mesmo tamanho.")

    if len(x_values) < 2:
        raise ValueError("São necessários pelo menos dois valores.")

    x_mean = mean(x_values)
    y_mean = mean(y_values)

    numerator = sum(
        (x - x_mean) * (y - y_mean)
        for x, y in zip(x_values, y_values)
    )

    x_variance = sum(
        (x - x_mean) ** 2
        for x in x_values
    )

    y_variance = sum(
        (y - y_mean) ** 2
        for y in y_values
    )

    denominator = (x_variance * y_variance) ** 0.5

    if denominator == 0:
        return 0.0

    return numerator / denominator