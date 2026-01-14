import urllib.request
from ..base import ExchangeTester

class LighterTester(ExchangeTester):
    def __init__(self):
        super().__init__("Lighter", "https://mainnet.zklighter.elliot.ai/health")

    def get_latency(self) -> float:
        try:
            return self._ping()
        except:
            # Fallback to base domain
            self.url = "https://mainnet.zklighter.elliot.ai/"
            return self._ping()
