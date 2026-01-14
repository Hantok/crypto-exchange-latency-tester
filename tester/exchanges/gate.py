from ..base import ExchangeTester

class GateTester(ExchangeTester):
    def __init__(self):
        super().__init__("Gate", "https://api.gateio.ws/api/v4/spot/time")

    def get_latency(self) -> float:
        return self._ping()
