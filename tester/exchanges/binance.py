import time
from ..base import ExchangeTester

class BinanceTester(ExchangeTester):
    def __init__(self):
        super().__init__("Binance", "https://api.binance.com/api/v3/ping")

    def get_latency(self) -> float:
        return self._ping()
