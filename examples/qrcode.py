import dhravyapy
import asyncio


async def main():
    # the text of the qrcode(can be links or just normal text)
    text = "https://api.dhravya.me"
    qrcode = await dhravyapy.Image().qrcode(text)
    # saving the image of the qrcode
    await qrcode.save("qrcode.png")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
