from ..base import ExchangeTester

class AsterTester(ExchangeTester):
    def __init__(self):
        super().__init__("Aster", "https://fapi.asterdex.com/fapi/v1/ping")

    def get_latency(self, url: str) -> float:
        return self._ping(url)
