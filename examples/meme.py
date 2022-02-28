import dhravyapy
import asyncio

async def main():
    meme = await dhravyapy.Meme().save("examplememe.png")
    print(meme.url)


if __name__ == __main__:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
