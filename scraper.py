import requests
from bs4 import BeautifulSoup

def buscar_preco(modelo):
    modelo_formatado = modelo.lower().replace(" ", "-")
    url = f"https://hwpriceguide.com/{modelo_formatado}/"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return None

    soup = BeautifulSoup(response.text, "html.parser")
    titulo = soup.find("h1", class_="entry-title")
    preco = soup.find("strong", string=lambda t: "Average Price:" in t if t else False)

    return {
        "nome": titulo.text.strip() if titulo else modelo,
        "preco_usd": preco.text.replace("Average Price:", "").strip() if preco else "N/A",
        "url": url
    }