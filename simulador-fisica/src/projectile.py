import math


class Projectile:
    """Modelo físico de um lançamento oblíquo."""

    GRAVITY = 9.81

    def __init__(self, initial_velocity: float, angle_degrees: float):
        if initial_velocity <= 0:
            raise ValueError("A velocidade inicial deve ser maior que zero.")

        if not 0 < angle_degrees < 90:
            raise ValueError("O ângulo deve estar entre 0 e 90 graus.")

        self.initial_velocity = initial_velocity
        self.angle_degrees = angle_degrees

        self.angle_radians = math.radians(angle_degrees)

        self.vx = (
            initial_velocity * math.cos(self.angle_radians)
        )
        self.vy = (
            initial_velocity * math.sin(self.angle_radians)
        )

    @property
    def flight_time(self) -> float:
        """Tempo total de voo, considerando lançamento e queda no mesmo nível."""
        return (2 * self.vy) / self.GRAVITY

    @property
    def maximum_height(self) -> float:
        """Altura máxima atingida pelo projétil."""
        return (self.vy ** 2) / (2 * self.GRAVITY)

    @property
    def range(self) -> float:
        """Alcance horizontal do lançamento."""
        return self.vx * self.flight_time

    def position(self, time: float) -> tuple[float, float]:
        """Retorna a posição (x, y) no instante informado."""

        if time < 0:
            raise ValueError("O tempo não pode ser negativo.")

        x = self.vx * time
        y = self.vy * time - 0.5 * self.GRAVITY * time ** 2

        return x, y

    def velocity(self, time: float) -> tuple[float, float]:
        """Retorna as componentes da velocidade no instante informado."""

        if time < 0:
            raise ValueError("O tempo não pode ser negativo.")

        vx = self.vx
        vy = self.vy - self.GRAVITY * time

        return vx, vy