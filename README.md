# Usage
```python
from bincentive_trader.client import TraderClient
import ccxt 

email = 'me@example.com'
password = 'super secret'
testing = True  # Change this to False if you're using mainnet. 

client = TraderClient(email, password, testing)

bitmex = ccxt.bitmex()

strategy_close_average_v1(bitmex,client,129,3,'XBTUSD','BTC',1,leverage=1)

```

Available strategies are:
- strategy_close_average_v1(instance,client,strategy_id, exchange_id, base_currency, quote_currency, amount,leverage=None, timeout=None, interval = 0)
- strategy_close_average_v2(instance,client,strategy_id, exchange_id, base_currency, quote_currency, amount,leverage=None, timeout=None, interval = 0, days = 3)
