from ..base import ExchangeTester

class MEXCTester(ExchangeTester):
    def __init__(self):
        super().__init__("MEXC", "https://api.mexc.com/api/v3/time")

    def get_latency(self) -> float:
        return self._ping()
