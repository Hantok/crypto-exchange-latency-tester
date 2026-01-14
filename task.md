# Crypto Exchange Latency Tester

I have implemented a command-line tool that measures and reports connection latency to 11 different crypto exchange APIs. The tool is designed to be easily extensible and runs tests concurrently for speed.

## Project Structure
- `tester/base.py`: The abstract base class providing the common logic and latency categorization.
- `tester/main.py`: The entry point that orchestrates concurrent testing using `asyncio.to_thread`.
- `tester/exchanges/`: Modular implementation for each exchange (Binance, Bybit, OKX, etc.).

## How to Run
The tool uses Python's standard library to ensure it works in any environment without installing extra packages.

```bash
cd /root/bots/latency-tester
export PYTHONPATH=$PYTHONPATH:.
python3 -m tester.main
```

## Example Output
The output is sorted by latency (lowest first) and color-coded based on the performance:
- **SUPREME**: < 20ms
- **GOOD**: 20ms - 50ms
- **NORMAL**: 50ms - 100ms
- **BAD**: > 100ms

```text
--------------------------------------------------
Exchange        | Latency (ms) | Status    
--------------------------------------------------
BingX           | 195.90       | BAD       
Bybit           | 207.60       | BAD       
OKX             | 233.36       | BAD       
Aster           | 248.48       | BAD       
Binance         | 265.39       | BAD       
MEXC            | 292.31       | BAD       
Bitget          | 294.94       | BAD       
KuCoin          | 323.63       | BAD       
Hyperliquid     | 484.65       | BAD       
Gate            | 999.00       | BAD       
Lighter         | N/A          | ERROR      (Error: <urlopen error [Errno -2] Name or service not known>)
--------------------------------------------------
```

## Adding a New Exchange
To add a new exchange, simply create a new file in `tester/exchanges/` following this pattern:

```python
from ..base import ExchangeTester

class MyNewExchangeTester(ExchangeTester):
    def __init__(self):
        super().__init__("MyExchange", "https://api.myexchange.com/ping")

    def get_latency(self) -> float:
        return self._ping()
```

Then register it in `tester/main.py`.
