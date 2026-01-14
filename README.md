# Crypto Exchange Latency Tester

A lightweight, concurrent Python utility to measure connection latency (ping) to various cryptocurrency exchange APIs. This tool helps high-frequency traders (HFT) and bot developers identify the best server locations for their trading infrastructure.

## 🚀 Features

- **Blazing Fast**: Uses `asyncio` with threading to test multiple exchanges concurrently.
- **Zero Dependencies**: Built using Python's standard library (`urllib`). No `pip install` required.
- **Visual Feedback**: Color-coded output based on latency performance.
- **Auto-Sorted**: Results are automatically sorted from lowest to highest latency.
- **Easy to Extend**: Simple plugin-like architecture for adding new exchanges.

## 📊 Latency Categorization

| Status | Range | Color |
| :--- | :--- | :--- |
| **SUPREME** | < 20ms | Magenta |
| **GOOD** | 20ms - 50ms | Green |
| **NORMAL** | 50ms - 100ms | Blue |
| **BAD** | > 100ms | Red |

## 🛠 Supported Exchanges

- Binance
- Bybit
- Bitget
- OKX
- KuCoin
- Gate.io
- MEXC
- BingX
- Hyperliquid
- Aster DEX
- Lighter.xyz

## 💻 Usage

No installation is required beyond having Python 3.11+ installed.

### Run the script:

```bash
# Clone the repository (if applicable)
# git clone <your-repo-url>
# cd latency-tester

# Run the tester
export PYTHONPATH=$PYTHONPATH:.
python3 -m tester.main
```

## ➕ Adding New Exchanges

To add a new exchange, create a new file in `tester/exchanges/`:

```python
from ..base import ExchangeTester

class MyExchangeTester(ExchangeTester):
    def __init__(self):
        super().__init__("MyExchange", "https://api.myexchange.com/v1/ping")

    def get_latency(self) -> float:
        return self._ping()
```

Then, register it in `tester/main.py`.

## 📄 License

MIT
