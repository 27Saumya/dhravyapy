import dhravyapy
import asyncio

async def main():
    truth = dhravyapy.TruthOrDare().truth
    dare = dhravyapy.TruthOrDare().dare
    print(f"If you wanted dare here is a dare : {dare}")
    print(f"If you wanted a truth here is a truth : {truth}")

if __name__ == __main__:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
