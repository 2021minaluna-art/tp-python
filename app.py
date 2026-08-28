from flask import Flask, render_template, request

app = Flask(__name__)


def dar_consejo(temperatura, llueve):

    if temperatura < 10:
        consejo = "Hace mucho frío."
        prendas = ["Abrigo", "Guantes", "Bufanda", "Gorro"]

    elif temperatura <= 25:
        consejo = "El día está agradable."
        prendas = ["Campera liviana", "Pantalón"]

    else:
        consejo = "Hace calor."
        prendas = ["Remera corta", "Shorts"]

    if llueve == "s":
        consejo += " Como está lloviendo, también llevá un paraguas."
        prendas.append("Paraguas")

    return consejo, prendas


@app.route("/", methods=["GET", "POST"])
def inicio():

    consejo = None
    prendas = []

    if request.method == "POST":

        temperatura = int(request.form["temperatura"])
        llueve = request.form["llueve"]

        consejo, prendas = dar_consejo(temperatura, llueve)

    return render_template(
        "index.html",
        consejo=consejo,
        prendas=prendas
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)