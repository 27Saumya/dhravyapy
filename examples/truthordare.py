import dhravyapy
import asyncio


async def main():
    tod = dhravyapy.Fun.truthordare()

    # getting truth or dare from the api
    truth = tod.truth
    dare = tod.dare

    # simple use case
    prompt = input("Truth or dare?")
    if prompt.lower() == "dare":
        print(f"Here is a dare : {dare}")
    elif prompt.lower() == "truth":
        print(f"Here is a truth : {truth}")
    else:
        print("Enter either truth or dare")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
