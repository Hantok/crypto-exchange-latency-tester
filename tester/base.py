import time
import urllib.request
import urllib.error
import json
from abc import ABC, abstractmethod

class ExchangeTester(ABC):
    def __init__(self, name: str, url: str, method: str = "GET", data: dict = None):
        self.name = name
        self.url = url
        self.method = method
        self.data = data

    @abstractmethod
    def get_latency(self) -> float:
        """Measure latency to the exchange. Returns latency in milliseconds."""
        pass

    def measure(self) -> dict:
        try:
            latency = self.get_latency()
            return {
                "name": self.name,
                "latency": latency,
                "status": self._get_status(latency),
                "error": None
            }
        except Exception as e:
            return {
                "name": self.name,
                "latency": float('inf'),
                "status": "ERROR",
                "error": str(e)
            }

    def _get_status(self, latency: float) -> str:
        if latency < 20:
            return "SUPREME"
        elif latency < 50:
            return "GOOD"
        elif latency < 100:
            return "NORMAL"
        else:
            return "BAD"

    def _ping(self) -> float:
        start_time = time.perf_counter()
        req = urllib.request.Request(self.url, method=self.method)
        if self.data:
            req.add_header('Content-Type', 'application/json')
            json_data = json.dumps(self.data).encode('utf-8')
            with urllib.request.urlopen(req, data=json_data, timeout=5) as response:
                response.read()
        else:
            with urllib.request.urlopen(req, timeout=5) as response:
                response.read()
        end_time = time.perf_counter()
        return (end_time - start_time) * 1000
