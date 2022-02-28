import dhravyapy
import asyncio

async def main():
    tod = dhravyapy.Fun.truthordare()
    truth = tod.truth
    dare = tod.dare
    print(f"If you want dare... here is a dare : {dare}")
    print(f"If you want a truth... here is a truth : {truth}")

if __name__ == __main__:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
