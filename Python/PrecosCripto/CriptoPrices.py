import requests

# Defina as URLs da API da Binance para o pares de negociação
btc_usd_url = 'https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT'
btc_brl_url = 'https://api.binance.com/api/v3/ticker/price?symbol=BTCBRL'

eth_usd_url = 'https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT'
eth_brl_url = 'https://api.binance.com/api/v3/ticker/price?symbol=ETHBRL'

ada_usd_url = 'https://api.binance.com/api/v3/ticker/price?symbol=ADAUSDT'
ada_brl_url = 'https://api.binance.com/api/v3/ticker/price?symbol=ADABRL'

# Função para obter o preço de um determinado par de negociação
def get_price(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        price = float(data['price'])
        return round(price, 2)
    else:
        return None

# Obtenha o preço do Bitcoin em USDT e BRL
btc_price = get_price(btc_usd_url)
if btc_price is not None:
    print(f"Preço do Bitcoin (BTC):", btc_price, "US$")
else:
    print('Falha ao obter o preço do Bitcoin em dolar')
    
btc_price = get_price(btc_brl_url)
if btc_price is not None:
    print(f"Preço do Bitcoin (BTC):", btc_price, "R$ \n")
else:
    print('Falha ao obter o preço do Bitcoin em reais \n')

# Obtenha o preço do Ethereum em USDT e BRL
eth_price = get_price(eth_usd_url)
if eth_price is not None:
    print(f"Preço do Etherium (ETH):", eth_price, "US$")
else:
    print('Falha ao obter o preço do Ethereum em dolar')
    
eth_price = get_price(eth_brl_url)
if eth_price is not None:
    print(f"Preço do Etherium (ETH):", eth_price, "R$ \n")
else:
    print('Falha ao obter o preço do Ethereum em reais \n')
    
# Obtenha o preço da Cardano em USDT e BRL
ada_price = get_price(ada_usd_url)
if ada_price is not None:
    print(f"Preço da Cardano (ADA):", ada_price, "US$")
else:
    print('Falha ao obter o preço da Cardano em dolar')
    
ada_price = get_price(ada_brl_url)
if ada_price is not None:
    print(f"Preço da Cardano (ADA):", ada_price, "R$ \n")
else:
    print('Falha ao obter o preço da Cardano em reais \n')
