# Usage
```python
from bincentive_trader.client import TraderClient
import ccxt 

email = 'me@example.com'
password = 'super secret'

client = TraderClient(email, password, False)

bitmex = ccxt.bitmex()
strategyId = 129
bitmexId = 3

strategy_close_average_v1(bitmex,client,strategyId,bitmexId,'XBTUSD','BTC',1,leverage=1)

```

Available strategies are:
- strategy_close_average_v1(instance,client,strategy_id, exchange_id, base_currency, quote_currency, amount,leverage=None, timeout=None, interval = 0)
- strategy_close_average_v2(instance,client,strategy_id, exchange_id, base_currency, quote_currency, amount,leverage=None, timeout=None, interval = 0, days = 3)
