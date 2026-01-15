import urllib.request
from ..base import ExchangeTester

class LighterTester(ExchangeTester):
    def __init__(self):
        super().__init__("Lighter", [
            "https://mainnet.zklighter.elliot.ai/health",
            "https://mainnet.zklighter.elliot.ai/"
        ])

    def get_latency(self, url: str) -> float:
        return self._ping(url)
