from ..base import ExchangeTester

class BingXTester(ExchangeTester):
    def __init__(self):
        super().__init__("BingX", "https://open-api.bingx.com/openApi/swap/v2/quote/time")

    def get_latency(self, url: str) -> float:
        return self._ping(url)
