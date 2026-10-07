import matplotlib.pyplot as plt

from projectile import Projectile


def plot_trajectory(projectile: Projectile) -> None:
    """Gera o gráfico da trajetória do projétil."""

    flight_time = projectile.flight_time
    number_of_points = 200

    times = [
        flight_time * i / (number_of_points - 1)
        for i in range(number_of_points)
    ]

    positions = [
        projectile.position(time)
        for time in times
    ]

    x_values = [position[0] for position in positions]
    y_values = [max(position[1], 0) for position in positions]

    plt.figure(figsize=(10, 6))

    plt.plot(
        x_values,
        y_values,
        linewidth=2,
        label=f"{projectile.angle_degrees:.1f}°"
    )

    plt.title("Trajetória do lançamento oblíquo")
    plt.xlabel("Distância horizontal (m)")
    plt.ylabel("Altura (m)")

    plt.grid(True, alpha=0.3)
    plt.legend()

    plt.tight_layout()
    plt.show()


def main():
    print("=" * 50)
    print("GRÁFICO DE TRAJETÓRIA")
    print("=" * 50)

    velocity = float(input("Velocidade inicial (m/s): "))
    angle = float(input("Ângulo de lançamento (graus): "))

    projectile = Projectile(velocity, angle)

    print("\nGerando gráfico...")

    plot_trajectory(projectile)


if __name__ == "__main__":
    main()