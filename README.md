<div align="center">
Deprecated [API no longer exists]
</div>


<div align="center">
<a href="https://pypi.org/project/dhravyapy">
    <img alt="Downloads" src="https://img.shields.io/pypi/dw/dhravyapy?color=blue">
</div>

## DhravyaPy is a basic, asynchronous wrapper for the [DhravyaAPI](https://api.dhravya.me)

### DhravyaPy works with [Python 3.8+](https://python.org)

### Features
  * Easy to use OOP design
  * Get random jokes
  * Get random topics
  * Generate images and memes
  * And much more!

### Installation
To install the library through [PyPi](https://pypi.org) use:-
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
    joke = await dhravya.Fun.joke()
    print(joke)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
```

To generate a qrcode
```py
import dhravyapy
import asyncio

async def main():
    # the text of the qrcode(can be links or just normal text)
    text = "https://api.dhravya.me" 
    qrcode = await dhravya.Image.qrcode(text)
    # saving the image of the qrcode
    await qrcode.save("qrcode.png")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
```

For more examples check out the [examples](https://github.com/27Saumya/dhravyapy/examples) directory.
