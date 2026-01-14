import time
from ..base import ExchangeTester

class BitgetTester(ExchangeTester):
    def __init__(self):
        super().__init__("Bitget", "https://api.bitget.com/api/v2/public/time")

    def get_latency(self) -> float:
        return self._ping()
