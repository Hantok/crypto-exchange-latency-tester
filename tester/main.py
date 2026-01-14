import asyncio
from .exchanges.binance import BinanceTester
from .exchanges.bybit import BybitTester
from .exchanges.bitget import BitgetTester
from .exchanges.okx import OKXTester
from .exchanges.kucoin import KuCoinTester
from .exchanges.gate import GateTester
from .exchanges.mexc import MEXCTester
from .exchanges.bingx import BingXTester
from .exchanges.hyperliquid import HyperliquidTester
from .exchanges.aster import AsterTester
from .exchanges.lighter import LighterTester

# ANSI color codes
COLORS = {
    "SUPREME": "\033[95m",  # Magenta/Purple
    "GOOD": "\033[92m",     # Green
    "NORMAL": "\033[94m",   # Blue
    "BAD": "\033[91m",      # Red
    "ERROR": "\033[90m",    # Gray
    "RESET": "\033[0m"
}

async def run_tests():
    testers = [
        BinanceTester(),
        BybitTester(),
        BitgetTester(),
        OKXTester(),
        KuCoinTester(),
        GateTester(),
        MEXCTester(),
        BingXTester(),
        HyperliquidTester(),
        AsterTester(),
        LighterTester()
    ]

    print(f"\n{'-'*50}")
    print(f"{'Exchange':<15} | {'Latency (ms)':<12} | {'Status':<10}")
    print(f"{'-'*50}")

    # Use asyncio.to_thread to run synchronous measure() calls concurrently
    tasks = [asyncio.to_thread(tester.measure) for tester in testers]
    results = await asyncio.gather(*tasks)

    # Sort by latency (float('inf') for errors will be last)
    sorted_results = sorted(results, key=lambda x: x['latency'])

    for res in sorted_results:
        name = res['name']
        latency = res['latency']
        status = res['status']
        error = res['error']

        color = COLORS.get(status, COLORS["RESET"])
        latency_str = f"{latency:.2f}" if latency != float('inf') else "N/A"
        
        row = f"{name:<15} | {latency_str:<12} | {color}{status:<10}{COLORS['RESET']}"
        if error:
            row += f" (Error: {error})"
        
        print(row)
    
    print(f"{'-'*50}\n")

if __name__ == "__main__":
    asyncio.run(run_tests())
