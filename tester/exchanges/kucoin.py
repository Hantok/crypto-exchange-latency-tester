from ..base import ExchangeTester

class KuCoinTester(ExchangeTester):
    def __init__(self):
        super().__init__("KuCoin", "https://api.kucoin.com/api/v1/timestamp")

    def get_latency(self, url: str) -> float:
        return self._ping(url)
