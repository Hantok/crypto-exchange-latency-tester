import time
import urllib.request
import urllib.error
import json
from abc import ABC, abstractmethod

class ExchangeTester(ABC):
    def __init__(self, name: str, url: str | list[str], method: str = "GET", data: dict = None):
        self.name = name
        self.urls = [url] if isinstance(url, str) else url
        self.method = method
        self.data = data

    @abstractmethod
    def get_latency(self, url: str) -> float:
        """Measure latency to the specific URL. Returns latency in milliseconds."""
        pass

    def measure(self) -> dict:
        best_result = {
            "name": self.name,
            "latency": float('inf'),
            "status": "ERROR",
            "error": "No reachable endpoints",
            "endpoint": None
        }

        for url in self.urls:
            try:
                # We need to pass the URL to get_latency, or set self.url temporarily
                self.curr_url = url 
                
                # Take minimum of 3 pings to filter out outliers/DNS misses
                pings = []
                for _ in range(3):
                    try:
                        pings.append(self.get_latency(url))
                    except:
                        pass
                
                if not pings:
                    continue # Try next URL

                latency = min(pings)
                
                if latency < best_result['latency']:
                    status = self._get_status(latency)
                    best_result = {
                        "name": self.name,
                        "latency": latency,
                        "status": status,
                        "error": None,
                        "endpoint": url
                    }
            except Exception as e:
                # If all fail, we want to keep the last error or a generic one
                if best_result['latency'] == float('inf'):
                     best_result['error'] = str(e)
        
        return best_result

    def _get_status(self, latency: float) -> str:
        if latency < 20:
            return "SUPREME"
        elif latency < 50:
            return "GOOD"
        elif latency < 100:
            return "NORMAL"
        else:
            return "BAD"

    def _ping(self, url: str = None) -> float:
        target_url = url if url else self.urls[0]
        start_time = time.perf_counter()
        req = urllib.request.Request(target_url, method=self.method)
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
