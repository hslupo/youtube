# %pip install yfinance

import yfinance, json

microsoft = yfinance.Ticker('MSF.DE')
daten = microsoft.info
print(json.dumps(daten, indent=4))

print(daten['regularMarketPrice'])

print(f'{daten["regularMarketPrice"]} {daten["currency"]}')

print(microsoft.history(period='1d', interval='1m')['Close'][-1])