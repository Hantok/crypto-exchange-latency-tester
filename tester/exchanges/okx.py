from ..base import ExchangeTester

class OKXTester(ExchangeTester):
    def __init__(self):
        super().__init__("OKX", "https://www.okx.com/api/v5/public/time")

    def get_latency(self) -> float:
        return self._ping()
