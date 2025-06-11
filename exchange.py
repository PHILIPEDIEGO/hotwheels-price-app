import requests

def converter_usd_para_brl(valor_usd):
    try:
        response = requests.get("https://economia.awesomeapi.com.br/json/last/USD-BRL")
        data = response.json()
        cotacao = float(data['USDBRL']['bid'])
        valor_usd_num = float(valor_usd.replace("$", "").strip())
        return round(valor_usd_num * cotacao, 2)
    except:
        return None