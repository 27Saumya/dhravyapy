import dhravyapy
import asyncio


async def main():
    trivia = await dhravyapy.Info.trivia()
    question = trivia.question
    answer = trivia.answer

    x = input(f"{question} \nType the answer...")

    if x.lower() == answer.lower():
        print("Good job you got the right answer!")
    else:
        print(":/ Lets do a different question")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
