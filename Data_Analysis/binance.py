import ccxt
import pandas as pd
import matplotlib.pyplot as plt


exchange = ccxt.binance()

symbol='ETH/USDT'
timeframe = '1d'

ohlvc = exchange.fetch_ohlcv(symbol,timeframe,limit=1000 )
data=pd.DataFrame(ohlvc,columns=['timestamp','open','high','low','close','volume'])
data['timestamp'] = pd.to_datetime(data['timestamp'],unit='ms')
data.set_index('timestamp',inplace=True)

max_price= data['high'].max()
min_price=data['low'].min()

diff = max_price - min_price
level1 = max_price - 0.236*diff
level2 = max_price - 0.382 * diff
level3 = max_price - 0.5 * diff
level4 = max_price - 0.618 * diff
level5 = max_price - 0.786 * diff

levels =[max_price,level1,level2,level3,level4,level5,min_price]

plt.figure(figsize=(12, 6))
plt.plot(data['close'],label = 'kapanış fiyatı',color ='blue')
plt.title(f'{symbol} fiyatı ve fibonacci düzeltme seviyeleri')

for level in levels:
    plt.axhline(level,linestyle='--',alpha=0.5,color='red')
    plt.text(data.index[-1],level,f'{level:.2f}', va='center',ha='right',color='red')


plt.xlabel('tarih')
plt.ylabel('fiyat (USDT)')
plt.legend()
plt.grid(True)
plt.show()