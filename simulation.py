import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

def compare_multiple_durations(durations=[4, 6, 10], return_fig=False):
    time_steps = 60
    arrival_rate = 10
    cars_per_sec = 1.2

    fig, ax = plt.subplots(figsize=(10, 6))

    for green_duration in durations:
        departure_rate = green_duration * cars_per_sec
        density = []
        current = 0
        for _ in range(time_steps):
            current += arrival_rate - departure_rate
            current = max(current, 0)
            density.append(current)
        ax.plot(density, label=f"Green={green_duration}s")

    ax.set_xlabel("Time (seconds)")
    ax.set_ylabel("Traffic Density")
    ax.set_title("Traffic Density for Different Green Durations")
    ax.legend()
    ax.grid(True)

    if return_fig:
        return fig
    else:
        plt.show()


def simulate_traffic_ode(green_duration=6, return_fig=False):
    def traffic_model(density, t, arrival_rate, departure_rate):
        return arrival_rate - departure_rate

    time = np.linspace(0, 60, 60)
    arrival_rate = 10
    departure_rate = green_duration * 1.2

    initial_density = 0
    density = odeint(traffic_model, initial_density, time, args=(arrival_rate, departure_rate)).flatten()
    density = np.clip(density, 0, None)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(time, density, label="Traffic Density (ODE)")
    ax.set_xlabel("Time (seconds)")
    ax.set_ylabel("Number of Vehicles")
    ax.set_title(f"Traffic Density via ODE (green={green_duration}s)")
    ax.grid(True)
    ax.legend()

    if return_fig:
        return fig
    else:
        plt.show()
