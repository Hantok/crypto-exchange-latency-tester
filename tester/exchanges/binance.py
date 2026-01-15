import time
from ..base import ExchangeTester

class BinanceTester(ExchangeTester):
    def __init__(self):
        super().__init__("Binance", [
            "https://api.binance.com/api/v3/ping",
            "https://api1.binance.com/api/v3/ping",
            "https://api2.binance.com/api/v3/ping",
            "https://api3.binance.com/api/v3/ping",
            "https://data-api.binance.vision/api/v3/ping"
        ])

    def get_latency(self, url: str) -> float:
        return self._ping(url)
