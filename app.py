from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "clave-secreta-tarea4"

# usuario de prueba, no hay base de datos todavia
USUARIO = "admin"
CLAVE = "1234"

# tareas en memoria
tareas = []
siguiente_id = 1


def logueado():
    return session.get("usuario") is not None


@app.route("/", methods=["GET"])
def inicio():
    if not logueado():
        return redirect("/login")
    return redirect("/tareas")


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        usuario = request.form.get("usuario", "")
        clave = request.form.get("clave", "")
        if usuario == USUARIO and clave == CLAVE:
            session["usuario"] = usuario
            return redirect("/tareas")
        else:
            error = "usuario o clave incorrectos"
    return render_template("login.html", error=error)


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


@app.route("/tareas", methods=["GET", "POST"])
def listar_tareas():
    global siguiente_id
    if not logueado():
        return redirect("/login")

    error = None
    if request.method == "POST":
        titulo = request.form.get("titulo", "").strip()
        if titulo == "":
            error = "el titulo no puede estar vacio"
        elif len(titulo) > 100:
            error = "el titulo es muy largo (max 100 caracteres)"
        else:
            tareas.append({"id": siguiente_id, "titulo": titulo, "completada": False})
            siguiente_id += 1

    return render_template("tareas.html", tareas=tareas, error=error)


@app.route("/tareas/<int:id_tarea>/editar", methods=["GET", "POST"])
def editar_tarea(id_tarea):
    if not logueado():
        return redirect("/login")

    tarea = next((t for t in tareas if t["id"] == id_tarea), None)
    if tarea is None:
        return render_template("error.html", mensaje="tarea no encontrada"), 404

    if request.method == "POST":
        titulo = request.form.get("titulo", "").strip()
        if titulo != "":
            tarea["titulo"] = titulo
        return redirect("/tareas")

    return render_template("editar.html", tarea=tarea)


@app.route("/tareas/<int:id_tarea>/eliminar", methods=["POST"])
def eliminar_tarea(id_tarea):
    if not logueado():
        return redirect("/login")

    global tareas
    tareas = [t for t in tareas if t["id"] != id_tarea]
    return redirect("/tareas")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
