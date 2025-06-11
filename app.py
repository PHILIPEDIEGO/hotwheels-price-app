from flask import Flask, render_template, request
from scraper import buscar_preco
from exchange import converter_usd_para_brl

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    if request.method == "POST":
        modelo = request.form["modelo"]
        dados = buscar_preco(modelo)
        if dados and dados["preco_usd"] != "N/A":
            preco_brl = converter_usd_para_brl(dados["preco_usd"])
            dados["preco_brl"] = f"R$ {preco_brl}" if preco_brl else "Erro ao converter"
        resultado = dados
    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)