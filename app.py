from flask import Flask, render_template_string
from datetime import datetime

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Reloj Flask</title>
    <script>
        function actualizarReloj() {
            const ahora = new Date();

            let horas = ahora.getHours().toString().padStart(2, '0');
            let minutos = ahora.getMinutes().toString().padStart(2, '0');
            let segundos = ahora.getSeconds().toString().padStart(2, '0');

            document.getElementById("reloj").innerHTML =
                horas + ":" + minutos + ":" + segundos;
        }

        setInterval(actualizarReloj, 1000);

        window.onload = actualizarReloj;
    </script>

    <style>
        body{
            display:flex;
            justify-content:center;
            align-items:center;
            height:100vh;
            font-family:Arial;
            background:#222;
            color:white;
        }

        h1{
            font-size:80px;
        }
    </style>
</head>

<body>

<h1 id="reloj"></h1>

</body>
</html>
"""

@app.route("/")
def inicio():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)