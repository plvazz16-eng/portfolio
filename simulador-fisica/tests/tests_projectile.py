import math
import sys
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"

sys.path.insert(0, str(SRC_PATH))

from projectile import Projectile


class TestProjectile(unittest.TestCase):

    def test_horizontal_velocity(self):
        projectile = Projectile(30, 45)
        expected = 30 * math.cos(math.radians(45))
        self.assertAlmostEqual(projectile.vx, expected, places=5)

    def test_vertical_velocity(self):
        projectile = Projectile(30, 45)
        expected = 30 * math.sin(math.radians(45))
        self.assertAlmostEqual(projectile.vy, expected, places=5)

    def test_flight_time(self):
        projectile = Projectile(30, 45)
        expected = (2 * 30 * math.sin(math.radians(45))) / 9.81
        self.assertAlmostEqual(projectile.flight_time, expected, places=5)

    def test_maximum_height(self):
        projectile = Projectile(30, 45)
        expected = (
            30 ** 2 * math.sin(math.radians(45)) ** 2
        ) / (2 * 9.81)
        self.assertAlmostEqual(projectile.maximum_height, expected, places=5)

    def test_range(self):
        projectile = Projectile(30, 45)
        expected = (30 ** 2 * math.sin(math.radians(90))) / 9.81
        self.assertAlmostEqual(projectile.range, expected, places=5)

    def test_position_at_launch(self):
        projectile = Projectile(30, 45)
        x, y = projectile.position(0)
        self.assertAlmostEqual(x, 0)
        self.assertAlmostEqual(y, 0)

    def test_invalid_velocity(self):
        with self.assertRaises(ValueError):
            Projectile(0, 45)

    def test_invalid_angle(self):
        with self.assertRaises(ValueError):
            Projectile(30, 100)


if __name__ == "__main__":
    unittest.main()