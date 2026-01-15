from ..base import ExchangeTester

class MEXCTester(ExchangeTester):
    def __init__(self):
        super().__init__("MEXC", "https://api.mexc.com/api/v3/time")

    def get_latency(self, url: str) -> float:
        return self._ping(url)
