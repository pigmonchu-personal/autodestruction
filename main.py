from flask import Flask, request, render_template, redirect
app = Flask(__name__)


datos = []
@app.route("/")
def inicio():
    # Recuperar datos del repositorio
    if len(datos):
        return '<br>'.join(datos)
    else:
        return "No hay datos"

@app.route("/nuevo", methods=["GET", "POST"])
def alta():
    if request.method == "GET":
        return render_template("alta.html")
    else:
        dato = request.form['dato']
        #validacion
        try:
            float(dato)
        except ValueError:
            return render_template("alta.html", error="Dato no numérico")
        
        datos.append(dato)
        return redirect("/")

