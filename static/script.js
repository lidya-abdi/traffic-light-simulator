function updateValue(val) {
    document.getElementById("durationValue").innerText = val;
}

function runSimulation() {
    const duration = document.getElementById("duration").value;
    document.getElementById("result").innerText = `Simulating for green duration: ${duration} seconds...`;

    // Trafik ışığı görseli
    const red = document.getElementById("redLight");
    const green = document.getElementById("greenLight");
    red.classList.remove("active");
    green.classList.add("active");

    setTimeout(() => {
        green.classList.remove("active");
        red.classList.add("active");
    }, duration * 1000);

    // Flask'a POST isteği gönder
    fetch('/simulate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: `duration=${duration}`
    })
    .then(response => response.blob())
    .then(blob => {
        const url = URL.createObjectURL(blob);
        const img = new Image();
        img.src = url;
        const chartArea = document.getElementById('chart');
        chartArea.innerHTML = '';
        chartArea.appendChild(img);
    })
    .catch(error => {
        console.error('Simulation failed:', error);
        document.getElementById("result").innerText = "Simulation failed. See console for details.";
    });
}
