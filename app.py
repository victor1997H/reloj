from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reloj Digital</title>

    <script>
        function actualizarReloj() {
            let ahora = new Date();

            let horas = ahora.getHours().toString().padStart(2, '0');
            let minutos = ahora.getMinutes().toString().padStart(2, '0');
            let segundos = ahora.getSeconds().toString().padStart(2, '0');

            document.getElementById("reloj").innerHTML =
                horas + ":" + minutos + ":" + segundos;
        }

        // Ejecuta la función cada segundo
        setInterval(actualizarReloj, 1000);
    </script>

    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            font-family: Arial, sans-serif;
            background: #222;
            color: white;
            margin: 0; /* Quita márgenes por defecto */
        }

        h1 {
            font-size: 15vw; /* Tamaño responsivo basado en el ancho de la pantalla */
            margin: 0;
        }
    </style>
</head>

<body>
    <h1 id="reloj">00:00:00</h1>
    
    <script>
        // Ejecuta la función inmediatamente apenas carga el HTML
        actualizarReloj();
    </script>
</body>
</html>
"""

@app.route("/")
def inicio():
    return render_template_string(HTML)

if __name__ == "__main__":
    # host="0.0.0.0" permite que lo veas desde tu celular usando la IP de tu PC
    app.run(host="0.0.0.0", port=5000)