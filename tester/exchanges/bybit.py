import time
from ..base import ExchangeTester

class BybitTester(ExchangeTester):
    def __init__(self):
        super().__init__("Bybit", [
            "https://api.bybit.com/v5/market/time",
            "https://api.bytick.com/v5/market/time"
        ])

    def get_latency(self, url: str) -> float:
        return self._ping(url)
