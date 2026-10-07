from projectile import Projectile


def main():
    print("=" * 50)
    print("SIMULADOR DE LANÇAMENTO OBLÍQUO")
    print("=" * 50)

    velocity = float(input("Velocidade inicial (m/s): "))
    angle = float(input("Ângulo de lançamento (graus): "))

    projectile = Projectile(velocity, angle)

    print("\n--- RESULTADOS ---")
    print(f"Velocidade inicial: {velocity:.2f} m/s")
    print(f"Ângulo: {angle:.2f}°")
    print(f"Componente horizontal: {projectile.vx:.2f} m/s")
    print(f"Componente vertical: {projectile.vy:.2f} m/s")
    print(f"Tempo de voo: {projectile.flight_time:.2f} s")
    print(f"Altura máxima: {projectile.maximum_height:.2f} m")
    print(f"Alcance: {projectile.range:.2f} m")

    print("\n--- POSIÇÕES ---")

    intervals = 10

    for i in range(intervals + 1):
        time = projectile.flight_time * i / intervals
        x, y = projectile.position(time)

        # Evita pequenos valores negativos causados por arredondamento.
        y = max(y, 0)

        print(
            f"t = {time:5.2f} s | "
            f"x = {x:7.2f} m | "
            f"y = {y:7.2f} m"
        )


if __name__ == "__main__":
    main()