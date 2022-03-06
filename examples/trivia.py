import dhravya
import asyncio


async def main():
    trivia = dhravya.Info().trivia()
    question = trivia.question
    ans = trivia.answer

    x = input(f"{question} \nType the answer...")

    if x.lower() == ans.lower():
        print("Good job you got the right answer!")
    else:
        print(":/ Lets do a different question")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
