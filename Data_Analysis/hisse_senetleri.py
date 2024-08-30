import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

# Örnek hisse senedi sembolü (örneğin Apple için AAPL)
ticker = 'DSAFDSAFDSFA'

# Veri aralığını belirleyelim (örneğin son 1 yıl)
start_date = '2023-01-01'
end_date = '2023-12-31'

# Hisse senedi verilerini Yahoo Finance üzerinden indirelim
data = yf.download(ticker, start=start_date, end=end_date)

# Verinin ilk birkaç satırını inceleyelim
print(data.head())

# Zaman serisi olarak kapanış fiyatlarını görselleştirelim
plt.figure(figsize=(10, 6))
plt.plot(data['Close'], label='Close Price')
plt.title(f'{ticker} Kapanış Fiyatı ({start_date} - {end_date})')
plt.xlabel('Tarih')
plt.ylabel('Fiyat (USD)')
plt.legend()
plt.grid(True)
plt.show()

# Basit hareketli ortalama (SMA) hesaplayalım
data['SMA_50'] = data['Close'].rolling(window=50).mean()

# Kapanış fiyatı ile birlikte SMA'yı görselleştirelim
plt.figure(figsize=(10, 6))
plt.plot(data['Close'], label='Close Price')
plt.plot(data['SMA_50'], label='50 Günlük SMA', linestyle='--')
plt.title(f'{ticker} Kapanış Fiyatı ve 50 Günlük SMA ({start_date} - {end_date})')
plt.xlabel('Tarih')
plt.ylabel('Fiyat (USD)')
plt.legend()
plt.grid(True)
plt.show()
