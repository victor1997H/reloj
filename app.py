from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# Base de datos temporal en memoria
tareas = ["Aprender Docker", "Configurar GitHub Actions", "Mejorar la interfaz Cyberpunk"]

HTML = """
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Panel Digital - Tareas</title>

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
    height: 60vh; /* Bajamos un poco el alto para dar espacio a las tareas */
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
    font-size: 40px;
    color: #00f5ff;
}

.hero-text p {
    margin-top: 20px;
    color: #aaa;
    line-height: 1.5;
}

/* FORMULARIO DE TAREAS */
.todo-form {
    margin-top: 25px;
    display: flex;
    gap: 10px;
}

.todo-input {
    background: rgba(0, 0, 0, 0.5);
    border: 1px solid #1f2a44;
    padding: 12px;
    color: white;
    border-radius: 8px;
    width: 70%;
    font-size: 14px;
}

.todo-input:focus {
    outline: none;
    border-color: #00f5ff;
    box-shadow: 0 0 10px rgba(0, 245, 255, 0.5);
}

/* BOTÓN */
.btn {
    display: inline-block;
    padding: 12px 25px;
    background: #00f5ff;
    color: black;
    border: none;
    border-radius: 8px;
    font-weight: bold;
    cursor: pointer;
    font-family: 'Orbitron', sans-serif;
}

.btn:hover {
    background: #00c2cc;
    box-shadow: 0 0 15px #00f5ff;
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

/* SECCIÓN DE TAREAS (Misma cuadrícula de tus tarjetas anteriores) */
.section-title {
    text-align: center;
    color: #00f5ff;
    margin-top: 20px;
    font-size: 24px;
}

.cards {
    display: flex;
    flex-wrap: wrap; /* Por si añades muchas tareas, bajarán ordenadamente */
    justify-content: center;
    gap: 20px;
    padding: 40px;
}

.card {
    width: 250px;
    min-height: 120px;
    background: #111a2e;
    border: 1px solid #1f2a44;
    border-radius: 10px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-between;
    padding: 15px;
    color: #fff;
    text-align: center;
    box-shadow: 0 4px 10px rgba(0,0,0,0.3);
}

.card-text {
    margin-bottom: 10px;
    font-size: 14px;
}

.btn-delete {
    background: transparent;
    border: 1px solid #ff4a4a;
    color: #ff4a4a;
    padding: 5px 10px;
    border-radius: 5px;
    cursor: pointer;
    font-size: 11px;
    font-weight: bold;
    transition: 0.3s;
}

.btn-delete:hover {
    background: #ff4a4a;
    color: white;
    box-shadow: 0 0 10px #ff4a4a;
}
</style>
</head>

<body>

<nav>
    <h2>Panel Digital</h2>
    <ul>
        <li>Inicio</li>
        <li>Tareas</li>
        <li>Servicios</li>
        <li>Contacto</li>
    </ul>
</nav>

<div class="hero">

    <div class="hero-text">
        <h1>Organizador de Tareas Futurista</h1>
        <p>
            Plataforma moderna desarrollada con Flask. Genera, administra y destruye tus objetivos diarios en tiempo real.
        </p>
        
        <form class="todo-form" action="/agregar" method="POST">
            <input type="text" name="nueva_tarea" class="todo-input" placeholder="Escribe un nuevo objetivo..." required autocomplete="off">
            <button type="submit" class="btn">Asignar</button>
        </form>
    </div>

    <div class="clock-box">
        <div id="reloj">00:00:00</div>
        <div id="fecha"></div>
    </div>

</div>

<h3 class="section-title">Objetivos Activos</h3>

<div class="cards">
    {% if tareas %}
        {% for tarea in tareas %}
        <div class="card">
            <div class="card-text">{{ tarea }}</div>
            <a href="/eliminar/{{ loop.index0 }}"><button class="btn-delete">Completado</button></a>
        </div>
        {% endfor %}
    {% else %}
        <div style="color: #aaa; font-style: italic;">No hay objetivos pendientes. ¡Buen trabajo!</div>
    {% endif %}
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
    # Enviamos la lista de tareas a la plantilla HTML
    return render_template_string(HTML, tareas=tareas)

@app.route("/agregar", methods=["POST"])
def agregar():
    tarea_recibida = request.form.get("nueva_tarea")
    if tarea_recibida:
        tareas.append(tarea_recibida) # Se añade a la lista
    return redirect(url_for("home"))

@app.route("/eliminar/<int:id>")
def eliminar(id):
    if 0 <= id < len(tareas):
        tareas.pop(id) # Se elimina por su índice
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)