from ..base import ExchangeTester

class OKXTester(ExchangeTester):
    def __init__(self):
        super().__init__("OKX", [
            "https://www.okx.com/api/v5/public/time",
            "https://okx.com/api/v5/public/time",
        ])

    def get_latency(self, url: str) -> float:
        return self._ping(url)
