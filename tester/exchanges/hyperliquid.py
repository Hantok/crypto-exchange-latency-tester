from ..base import ExchangeTester

class HyperliquidTester(ExchangeTester):
    def __init__(self):
        super().__init__("Hyperliquid", "https://api.hyperliquid.xyz/info", method="POST", data={"type": "meta"})

    def get_latency(self) -> float:
        return self._ping()
