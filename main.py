from visualization import plot_optimization_curve
from simulation import simulate_traffic_ode, compare_multiple_durations
import numpy as np
import matplotlib.pyplot as plt

def run_random_traffic_simulation(return_fig=False):
    time_steps = 60
    arrival_rate = np.random.randint(5, 15, size=time_steps)
    departure_rate = np.random.randint(3, 12, size=time_steps)

    traffic_density = []
    current_density = 0

    for i in range(time_steps):
        current_density += arrival_rate[i] - departure_rate[i]
        current_density = max(current_density, 0)
        traffic_density.append(current_density)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(traffic_density, label="Traffic Density")
    ax.plot(arrival_rate, '--', label="Arrival Rate (in)")
    ax.plot(departure_rate, '--', label="Departure Rate (out)")
    ax.set_xlabel("Time (seconds)")
    ax.set_ylabel("Number of Vehicles")
    ax.set_title("Random Traffic Density Simulation Over Time")
    ax.legend()
    ax.grid(True)

    if return_fig:
        return fig
    else:
        plt.show()


if __name__ == "__main__":
    # 1. Rastgele giriş/çıkış simülasyonu
    run_random_traffic_simulation()

    # 2. ODE tabanlı simülasyon
    simulate_traffic_ode(green_duration=6)

    # 3. Farklı ışık sürelerinin karşılaştırması
    compare_multiple_durations([4, 6, 10])

    # 4. Optimizasyon eğrisi
    plot_optimization_curve()
