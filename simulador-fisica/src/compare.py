import matplotlib.pyplot as plt

from projectile import Projectile


def compare_angles(velocity: float, angles: list[float]) -> None:
    """Compara trajetórias de projéteis para diferentes ângulos."""

    results = []

    for angle in angles:
        projectile = Projectile(velocity, angle)

        results.append({
            "angle": angle,
            "flight_time": projectile.flight_time,
            "max_height": projectile.maximum_height,
            "range": projectile.range,
        })

    print("\n" + "=" * 70)
    print("COMPARAÇÃO DE TRAJETÓRIAS")
    print("=" * 70)

    print(
        f"{'Ângulo':>10}"
        f"{'Tempo (s)':>15}"
        f"{'Altura (m)':>15}"
        f"{'Alcance (m)':>15}"
    )

    print("-" * 70)

    for result in results:
        print(
            f"{result['angle']:>9.1f}°"
            f"{result['flight_time']:>15.2f}"
            f"{result['max_height']:>15.2f}"
            f"{result['range']:>15.2f}"
        )

    best_range = max(results, key=lambda result: result["range"])

    print("\n" + "-" * 70)
    print(
        f"Maior alcance: {best_range['angle']:.1f}° "
        f"→ {best_range['range']:.2f} m"
    )

    plt.figure(figsize=(10, 6))

    for angle in angles:
        projectile = Projectile(velocity, angle)

        number_of_points = 200

        times = [
            projectile.flight_time * i / (number_of_points - 1)
            for i in range(number_of_points)
        ]

        positions = [
            projectile.position(time)
            for time in times
        ]

        x_values = [position[0] for position in positions]
        y_values = [max(position[1], 0) for position in positions]

        plt.plot(
            x_values,
            y_values,
            linewidth=2,
            label=f"{angle}°"
        )

    plt.title("Comparação de trajetórias")
    plt.xlabel("Distância horizontal (m)")
    plt.ylabel("Altura (m)")

    plt.grid(True, alpha=0.3)
    plt.legend(title="Ângulo")

    plt.tight_layout()
    plt.show()


def main():
    print("=" * 70)
    print("SIMULADOR DE LANÇAMENTO OBLÍQUO")
    print("=" * 70)

    velocity = float(input("\nVelocidade inicial (m/s): "))

    angles = [15, 30, 45, 60, 75]

    compare_angles(velocity, angles)


if __name__ == "__main__":
    main()