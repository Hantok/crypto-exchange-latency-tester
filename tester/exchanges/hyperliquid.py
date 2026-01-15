from ..base import ExchangeTester

class HyperliquidTester(ExchangeTester):
    def __init__(self):
        super().__init__("Hyperliquid", "https://api.hyperliquid.xyz/info", method="POST", data={"type": "meta"})

    def get_latency(self, url: str) -> float:
        return self._ping(url)
