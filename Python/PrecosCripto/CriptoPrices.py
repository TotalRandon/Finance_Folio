import requests 

from binance.client import Client 

# Substitua pelos seus próprios valores da API
api_key = 'MaQ9cRs4otjKtUZjMcR6jqu79xNj7JKEb6nf0Mg9PjJZKz6a4cG8diWfoae2EDcJ'
api_secret = '4fTWvBjDlirb0cUO4xqS6sE3sOpr1JqDoBPTBOs4c57fsjfUg5W4rnNX9vztYjxR'

## Criação da instância do cliente
client = Client(api_key, api_secret)

# Obtendo o preço atual das criptomoedas em relação ao dólar (USDT)
symbol_btc = 'BTCUSDT'
ticker_btc = client.get_symbol_ticker(symbol=symbol_btc)

symbol_eth = 'ETHUSDT'
ticker_eth = client.get_symbol_ticker(symbol=symbol_eth)

symbol_ada = 'ADAUSDT'
ticker_ada = client.get_symbol_ticker(symbol=symbol_ada)

# Verificando se a resposta da API foi bem-sucedida 
if 'price' in ticker_btc:
    btc_price = float(ticker_btc['price'])
    btc_price_rounded = round(btc_price, 2)
    print(f"Preço do Bitcoin (BTC): {btc_price_rounded}")
else:
    print("Erro ao obter o preço do Bitcoin")
    
if 'price' in ticker_eth:
    eth_price = float(ticker_eth['price'])
    eth_price_rounded = round(eth_price, 2)
    print(f"Preço do Etherium (ETH): {eth_price_rounded}")
else:
    print("Erro ao obter o preço do Etherium")
    
if 'price' in ticker_ada:
    ada_price = float(ticker_ada['price'])
    ada_price_rounded = round(ada_price, 2)
    print(f"Preço da Cardano (ETH): {ada_price_rounded}")
else:
    print("Erro ao obter o preço da Cardano")