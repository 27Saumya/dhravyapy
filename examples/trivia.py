import dhravyapy
import asyncio

async def main():
    trivia = dhravyapy.Info().trivia()
    question = trivia.question
    ans = trivia.answer

    x = input(f"{question} \n Type the answer...")

    if x.lower() == ans.lower():
        print("Good job you got the right answer")
    else:
        print(":/ Lets do a different answer next time")


if __name__ == __main__:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
