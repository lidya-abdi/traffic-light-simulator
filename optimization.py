from scipy.optimize import minimize_scalar

def total_density(green_duration, time_steps=60, arrival_rate=10, cars_per_sec=1.2):
    green_duration = int(green_duration)
    departure_rate = green_duration * cars_per_sec
    current_density = 0
    total_density_accumulated = 0

    for _ in range(time_steps):
        current_density += arrival_rate - departure_rate
        current_density = max(current_density, 0)
        total_density_accumulated += current_density

    return total_density_accumulated

def find_optimal_green_duration(time_steps=60, arrival_rate=10, cars_per_sec=1.2):
    result = minimize_scalar(
        lambda x: total_density(x, time_steps, arrival_rate, cars_per_sec),
        bounds=(1, 20),
        method='bounded'
    )
    print(f"En iyi yeşil süre: {result.x:.2f} saniye")
    print(f"Toplam yoğunluk (min): {result.fun:.2f}")
    return result
