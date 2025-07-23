import matplotlib.pyplot as plt
from optimization import total_density

def plot_optimization_curve(min_duration=1, max_duration=20, time_steps=60, arrival_rate=10, cars_per_sec=1.2, return_fig=False):
    durations = list(range(min_duration, max_duration + 1))
    densities = [total_density(d, time_steps, arrival_rate, cars_per_sec) for d in durations]

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(durations, densities, marker='o', linestyle='-', color='blue', label='Total Density')
    ax.set_title("Green Light Duration vs Total Traffic Density")
    ax.set_xlabel("Green Light Duration (seconds)")
    ax.set_ylabel("Total Accumulated Traffic Density")
    ax.grid(True)
    ax.legend()

    if return_fig:
        return fig
    else:
        plt.show()
