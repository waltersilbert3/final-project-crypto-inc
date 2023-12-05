import requests
import tkinter as tk

class CryptoCurrency:
    def __init__(self, name, symbol, price, market_cap, volume_24h):
        self.name = name
        self.symbol = symbol
        self.price = price
        self.market_cap = market_cap
        self.volume_24h = volume_24h

    def update_price(self, new_price):
        self.price = new_price

    def get_market_cap(self):
        return self.market_cap

    def get_volume_24h(self):
        return self.volume_24h

class CryptoTracker:
    def __init__(self, root):
        self.crypto_list = []
        self.initialize_currencies()
        self.root = root
        self.create_display()
        self.continuous_update_and_display()

    def initialize_currencies(self):
        btc = CryptoCurrency("Bitcoin", "BTC", 50000, 900_000_000_000, 100_000)
        xlm = CryptoCurrency("Stellar", "XLM", 0.4, 10_000_000_000, 20_000)
        eth = CryptoCurrency("Ethereum", "ETH", 4000, 500_000_000_000, 50_000)

        self.crypto_list = [btc, xlm, eth]

    def fetch_crypto_prices(self):
        coins_to_fetch = ['bitcoin', 'stellar', 'ethereum']

        for i, coin in enumerate(coins_to_fetch):
            url = f'https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd'
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                if coin == 'bitcoin':
                    btc_price = data['bitcoin']['usd']
                    self.crypto_list[i].update_price(btc_price)
                elif coin == 'stellar':
                    xlm_price = data['stellar']['usd']
                    self.crypto_list[i].update_price(xlm_price)
                elif coin == 'ethereum':
                    eth_price = data['ethereum']['usd']
                    self.crypto_list[i].update_price(eth_price)

    def create_display(self):
        self.root.title("Crypto Price Tracker")
        self.root.configure(bg="#ADD8E6")  # Set background color
        
        self.label = tk.Label(self.root, text="", font=("Alegreya", 12), bg="#ADD8E6", justify="left")
        self.label.pack(padx=20, pady=20)

    def update_display(self):
        info = "Current Crypto Prices:\n\n"
        for currency in self.crypto_list:
            info += f"{currency.name} ({currency.symbol}):\nPrice - ${currency.price}\nMarket Cap - {currency.market_cap}\nVolume (24h) - {currency.volume_24h}\n\n"
        self.label.config(text=info)

    def continuous_update_and_display(self):
        self.fetch_crypto_prices()
        self.update_display()
        self.root.after(60000, self.continuous_update_and_display)  # Update every 1 minute (60000 milliseconds)

class CryptoTrackerController:
    def __init__(self):
        self.root = tk.Tk()
        self.crypto_tracker = CryptoTracker(self.root)
        self.root.mainloop()


controller = CryptoTrackerController()