# DhravyaPy

## DhravyaPy is a basic, asynchronous wrapper for the [DhravyaAPI](https://api.dhravya.me)

### Features
  * Easy to use OOP
  * Get random jokes
  * Get random topics
  * Generate images and memes

### Prerequisites
  * Python 3.8+
  * requirements.txt

### Installation
To install the library through [PyPi](pypi.org) use:-
```
pip install dhravyapy
```

To install the development version(using git):-
```
pip install git+https://github.com/27Saumya/dhravyapy
```

### Examples
To get a random joke
```py
import dhravyapy
import asyncio

async def main():
    joke = await dhravyapy.Fun().joke()
    print(joke)


if __name__ == __main__:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
```

To generate a qrcode
```py
import dhravyapy
import asyncio

async def main():
    qrcode = await dhravyapy.Image().qrcode("https://api.dhravya.me")
    await qrcode.save("qrcode.png")


if __name__ == __main__:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
```
