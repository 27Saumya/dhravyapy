import dhravyapy
import asyncio

async def main():
    qrcode = await dhravyapy.Image().qrcode("https://api.dhravya.me")
    await qrcode.save("qrcode.png")


if __name__ == __main__:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
