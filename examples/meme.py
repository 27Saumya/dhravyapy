import dhravyapy
import asyncio

async def main():
    single_meme = await dhravyapy.Fun().single_meme() # Returns only the meme... no additional dict data.
    await single_meme.save()
    meme = await dhravyapy.Fun().meme("random")
    print(meme.url)


if __name__ == __main__:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
