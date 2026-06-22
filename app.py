from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Panel Digital</title>

<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;600;800&display=swap" rel="stylesheet">

<style>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Orbitron', sans-serif;
}

body {
    background: #0b0f1a;
    color: white;
    overflow-x: hidden;
}

/* NAVBAR */
nav {
    display: flex;
    justify-content: space-between;
    padding: 20px 60px;
    background: rgba(0,0,0,0.4);
    backdrop-filter: blur(10px);
    border-bottom: 1px solid #1f2a44;
}

nav h2 {
    color: #00f5ff;
}

nav ul {
    display: flex;
    gap: 20px;
    list-style: none;
}

nav ul li {
    cursor: pointer;
    color: #ccc;
}

/* HERO */
.hero {
    height: 90vh;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 60px;
    background: radial-gradient(circle at top, #1b2a4a, #0b0f1a);
}

/* TEXTO */
.hero-text {
    max-width: 600px;
}

.hero-text h1 {
    font-size: 50px;
    color: #00f5ff;
}

.hero-text p {
    margin-top: 20px;
    color: #aaa;
    line-height: 1.5;
}

/* BOTÓN */
.btn {
    margin-top: 30px;
    display: inline-block;
    padding: 12px 25px;
    background: #00f5ff;
    color: black;
    border-radius: 8px;
    font-weight: bold;
    cursor: pointer;
}

.btn:hover {
    background: #00c2cc;
}

/* RELOJ */
.clock-box {
    text-align: center;
    padding: 40px;
    border: 2px solid #00f5ff;
    border-radius: 20px;
    box-shadow: 0 0 30px #00f5ff;
    background: rgba(0,0,0,0.4);
}

#reloj {
    font-size: 60px;
    color: #00f5ff;
}

#fecha {
    margin-top: 10px;
    color: #ccc;
}

/* TARJETAS */
.cards {
    display: flex;
    justify-content: center;
    gap: 20px;
    padding: 40px;
}

.card {
    width: 200px;
    height: 120px;
    background: #111a2e;
    border: 1px solid #1f2a44;
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #00f5ff;
}
</style>
</head>

<body>

<nav>
    <h2>Panel Digital</h2>
    <ul>
        <li>Inicio</li>
        <li>Acerca de</li>
        <li>Servicios</li>
        <li>Contacto</li>
    </ul>
</nav>

<div class="hero">

    <div class="hero-text">
        <h1>Sistema Digital con Reloj en Tiempo Real</h1>
        <p>
            Plataforma moderna desarrollada con Flask.  
            Incluye un reloj dinámico en vivo con diseño futurista estilo panel tecnológico.
        </p>
        <div class="btn">Comenzar</div>
    </div>

    <div class="clock-box">
        <div id="reloj">00:00:00</div>
        <div id="fecha"></div>
    </div>

</div>

<div class="cards">
    <div class="card">Análisis</div>
    <div class="card">Rendimiento</div>
    <div class="card">Seguridad</div>
</div>

<script>
function actualizarReloj() {
    let ahora = new Date();

    let h = ahora.getHours().toString().padStart(2,'0');
    let m = ahora.getMinutes().toString().padStart(2,'0');
    let s = ahora.getSeconds().toString().padStart(2,'0');

    document.getElementById("reloj").innerHTML = h + ":" + m + ":" + s;

    let opciones = { weekday:'long', year:'numeric', month:'long', day:'numeric' };
    document.getElementById("fecha").innerHTML = ahora.toLocaleDateString('es-ES', opciones);
}

setInterval(actualizarReloj, 1000);
actualizarReloj();
</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)