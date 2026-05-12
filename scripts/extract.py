import requests
import pandas as pd
from datetime import datetime
import os

url = "https://api.coingecko.com/api/v3/coins/markets"

params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 10,
    "page": 1
}

response = requests.get(url, params=params)
data = response.json()

df = pd.DataFrame(data)

df = df[["id", "symbol", "current_price", "market_cap", "total_volume"]]

df["date"] = datetime.today().date()

file_name = "data/crypto_data.csv"

if os.path.exists(file_name):
    df.to_csv(file_name, mode='a', header=False, index=False)
else:
    df.to_csv(file_name, index=False)

print("Datos guardados")