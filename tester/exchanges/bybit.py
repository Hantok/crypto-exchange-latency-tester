import time
from ..base import ExchangeTester

class BybitTester(ExchangeTester):
    def __init__(self):
        super().__init__("Bybit", "https://api.bybit.com/v5/market/time")

    def get_latency(self) -> float:
        return self._ping()
