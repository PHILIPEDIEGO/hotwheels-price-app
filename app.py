import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hot Wheels Price App funcionando!</h1><p>Você pode integrar com o scraper aqui futuramente.</p>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)