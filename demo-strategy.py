import ccxt
import time
import numpy as np
import datetime
import pytz
from bincentive_trader.client import TraderClient


def get_real_close_data(instance,currency):
    """ Use ccxt to get the close and average price.
        :param instance: ccxt instrument object, e.g. ccxt.bitmex()
        :param currency: string, e.g. "BTC/USD"
        :return: float,close and average price 
    """
    instance_dic = instance.fetch_ticker(currency)
    close = instance_dic['close']
    average = instance_dic['average']
    return close,average

# average = (close+open)/2
def strategy_close_average_v1(instance,client,strategy_id, exchange_id, base_currency, quote_currency, amount,leverage=None, timeout=None, interval = 0):
    
    """Trade on a situation that whether the close price > (the last close price+ the last open price)/2.
        :param instance: ccxt instrument object, e.g. ccxt.bitmex()
        :param client: TraderClient object
        :param strategy_id: int
        :param exchange_id: int
        :param base_currency: e.g., 'XBTUSD'
        :param quote_currency: e.g., 'BTC'
        :param side: 'BUY' or 'SELL'
        :param amount: the amount to sell or buy
        :param leverage: bitmex exchange leverage
        :param timeout: request timeout
        :param interval: int, the time interval(seconds) between two orders
        :return: None.
    """
    currency = quote_currency+'/'+base_currency[3:]
    _, average_last = get_real_close_data(instance,currency)
    while(True):
        close,average = get_real_close_data(instance,currency)
        if(close>average_last):
            print(f'Buy {amount} {currency} at {close}')
            state = client.add_market_order(strategy_id, exchange_id, base_currency, quote_currency, 'BUY', amount, leverage, timeout)
        else:
            print(f'Sell {amount} {currency} at {close}')
            state = client.add_market_order(strategy_id, exchange_id, base_currency, quote_currency, 'SELL', amount, leverage, timeout)
        if(state == False): 
            print('Error!')
            break
        average_last = average
        time.sleep(interval)

# Real average
def strategy_close_average_v2(instance,client,strategy_id, exchange_id, base_currency, quote_currency, amount,leverage=None, timeout=None, interval = 0, days = 3):
    """Trade on a situation that whether the close price > the average of the close price.
        :param instance: ccxt instrument object, e.g. ccxt.bitmex()
        :param client: TraderClient object
        :param strategy_id: int
        :param exchange_id: int
        :param base_currency: e.g., 'XBTUSD'
        :param quote_currency: e.g., 'BTC'
        :param side: 'BUY' or 'SELL'
        :param amount: the amount to sell or buy
        :param leverage: bitmex exchange leverage
        :param timeout: request timeout
        :param interval: int, the time interval(seconds) between two orders
        :param days:int, the number of days to caculate the average
        :return: None.
    """
    currency = quote_currency+'/'+base_currency[3:]
    close_list = np.array([])
    
    while(close_list.shape[0] < days):
        close_list = np.append(close_list, instance.fetch_ticker(currency)['close'])
        time.sleep(time_stamp)
    
    while(True):
        close = instance.fetch_ticker(currency)['close']
        average = close_list.mean()
        close_list = np.append(close_list[1:],close)
        if(close>average):
            print(f'Buy {amount} {currency} at {close}')
            state = client.add_market_order(strategy_id, exchange_id, base_currency, quote_currency, 'BUY', amount, leverage, timeout)
        else:
            print(f'Sell {amount} {currency} at {close}')
            state = client.add_market_order(strategy_id, exchange_id, base_currency, quote_currency, 'SELL', amount, leverage, timeout)
        if(state == False): 
            print('Error!')
            break
            
        time.sleep(time_stamp)


        
### Some examples
email = 'xxx'
password = 'xxx'
testing = True  # Change this to False if you're using mainnet. 

client = TraderClient(email, password, testing)
bitmex = ccxt.bitmex()
strategy_close_average_v1(bitmex,client,129,3,'XBTUSD','BTC',1,leverage=1)