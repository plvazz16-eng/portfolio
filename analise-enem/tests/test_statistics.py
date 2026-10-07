import sys
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"

sys.path.insert(0, str(SRC_PATH))

from stats import (
    calculate_correlation,
    calculate_mean,
    calculate_median,
    calculate_standard_deviation,
)


class TestStatistics(unittest.TestCase):

    def test_mean(self):
        values = [10, 20, 30, 40, 50]

        result = calculate_mean(values)

        self.assertEqual(result, 30)

    def test_median(self):
        values = [10, 20, 30, 40, 50]

        result = calculate_median(values)

        self.assertEqual(result, 30)

    def test_median_even_list(self):
        values = [10, 20, 30, 40]

        result = calculate_median(values)

        self.assertEqual(result, 25)

    def test_standard_deviation(self):
        values = [10, 20, 30]

        result = calculate_standard_deviation(values)

        self.assertAlmostEqual(
            result,
            10,
            places=5,
        )

    def test_perfect_positive_correlation(self):
        x_values = [1, 2, 3, 4, 5]
        y_values = [2, 4, 6, 8, 10]

        result = calculate_correlation(
            x_values,
            y_values,
        )

        self.assertAlmostEqual(
            result,
            1.0,
            places=5,
        )

    def test_perfect_negative_correlation(self):
        x_values = [1, 2, 3, 4, 5]
        y_values = [10, 8, 6, 4, 2]

        result = calculate_correlation(
            x_values,
            y_values,
        )

        self.assertAlmostEqual(
            result,
            -1.0,
            places=5,
        )

    def test_different_lengths(self):
        with self.assertRaises(ValueError):
            calculate_correlation(
                [1, 2, 3],
                [1, 2],
            )

    def test_insufficient_data(self):
        with self.assertRaises(ValueError):
            calculate_correlation(
                [1],
                [2],
            )


if __name__ == "__main__":
    unittest.main()