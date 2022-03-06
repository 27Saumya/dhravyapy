import dhravya
import asyncio


async def main():
    # returns only the meme, no additional dict data
    single_meme = await dhravya.Fun().single_meme()
    # saving the meme image
    await single_meme.save()

    # getting a meme from a query string
    meme = await dhravya.Fun().meme("random")
    print(meme.url)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
