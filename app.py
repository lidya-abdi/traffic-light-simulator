from flask import Flask, render_template, request, send_file
import matplotlib.pyplot as plt
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('traffic_simulator.html')

@app.route('/simulate', methods=['POST'])
def simulate():
    green_duration = int(request.form['duration'])

    # Basit örnek grafik
    fig, ax = plt.subplots()
    t = list(range(60))
    y = [max(0, (10 - green_duration * 1.2) * i) for i in t]
    ax.plot(t, y)
    ax.set_title(f"Green Duration: {green_duration}s")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Vehicle Accumulation")

    # Görseli döndür
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    return send_file(buf, mimetype='image/png')

@app.route('/optimization-curve')
def optimization_curve():
    from visualization import plot_optimization_curve
    import io

    fig = plot_optimization_curve(return_fig=True)
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    return send_file(buf, mimetype='image/png')

@app.route('/random-simulation')
def random_simulation():
    from main import run_random_traffic_simulation
    fig = run_random_traffic_simulation(return_fig=True)
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    return send_file(buf, mimetype='image/png')

@app.route('/traffic-ode')
def traffic_ode():
    from simulation import simulate_traffic_ode
    fig = simulate_traffic_ode(green_duration=6, return_fig=True)
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    return send_file(buf, mimetype='image/png')

@app.route('/compare-durations')
def compare_durations():
    from simulation import compare_multiple_durations
    fig = compare_multiple_durations(return_fig=True)
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    return send_file(buf, mimetype='image/png')


if __name__ == '__main__':
    app.run(debug=True)
