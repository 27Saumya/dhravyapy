"""
MIT License

Copyright (c) 2022 27Saumya

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from .http import HTTPClient
from typing import *
from .errors import *
from .assets import Animal, GeneralImage


class Image:
    """
    The class to get Image data from the API
    """

    @classmethod
    async def cat(cls) -> Animal:
        """
        :class:`GeneralImage` Gets a random cat picture.
        """
        response = await HTTPClient().get("cat")

        if response.status == 200:
            return Animal(await response.read())

        else:
            raise HTTPException(f"HTTP Error: {response.status}")

    @classmethod
    async def dog(cls) -> Animal:
        """
        :class:`GeneralImage` Gets a random dog picture.
        """
        response = await HTTPClient().get("dog")

        if response.status == 200:
            return Animal(await response.read())

        else:
            raise HTTPException(f"HTTP Error: {response.status}")

    @classmethod
    async def fox(cls) -> Animal:
        """
        :class:`GeneralImage` Gets a random fox picture.
        """
        response = await HTTPClient().get("fox")

        if response.status == 200:
            return Animal(await response.read())

        else:
            raise HTTPException(f"HTTP Error: {response.status}")

    @classmethod
    async def create_meme(cls, top: str, bottom: str, image: Optional[str] = None) -> GeneralImage:
        """
        :class:`GeneralImage` Creates a meme image.
        """
        response = await HTTPClient().get(f"meme?top={top}&bottom={bottom}&image={image}")

        if response.status == 200:
            return GeneralImage(await response.read())

        elif response.status == 422:
            raise ValidationError("Recieved an invalid input")

        else:
            raise HTTPException(f"HTTP Error: {response.status}")

    @classmethod
    async def mealsome(cls, me: str, alsome: str) -> GeneralImage:
        """
        :class:`GeneralImage` Creates a me - also me meme image.
        """
        response = await HTTPClient().get(f"mealsome?me={me}&alsome={alsome}")

        if response.status == 200:
            return GeneralImage(await response.read())

        elif response.status == 422:
            raise ValidationError("Recieved an invalid input")

        else:
            raise HTTPException(f"HTTP Error: {response.status}")

    @classmethod
    async def itsretarded(cls, text: str) -> GeneralImage:
        """
        :class:`GeneralImage` Creates a retarded meme image.
        """
        response = await HTTPClient().get(f"itsretarded?text={text}")

        if response.status == 200:
            return GeneralImage(await response.read())

        elif response.status == 422:
            raise ValidationError("Recieved an invalid input")

        else:
            raise HTTPException(f"HTTP Error: {response.status}")

    @classmethod
    async def headache(cls, text: str) -> GeneralImage:
        """
        :class:`GeneralImage` Creates a headache meme image.
        """
        response = await HTTPClient().get(f"headache?text={text}")

        if response.status == 200:
            return GeneralImage(await response.read())

        elif response.status == 422:
            raise ValidationError("Recieved an invalid input")

        else:
            raise HTTPException(f"HTTP Error: {response.status}")

    @classmethod
    async def classnote(cls, text: str) -> GeneralImage:
        """
        :class:`GeneralImage` Creates a classnote meme image.
        """
        response = await HTTPClient().get(f"classnote?text={text}")

        if response.status == 200:
            return GeneralImage(await response.read())

        elif response.status == 422:
            raise ValidationError("Recieved an invalid input")

        else:
            raise HTTPException(f"HTTP Error: {response.status}")

    @classmethod
    async def nutbutton(cls, text: str) -> GeneralImage:
        """
        :class:`GeneralImage` Creates a nutbutton meme image.
        """
        response = await HTTPClient().get(f"nutbutton?text={text}")

        if response.status == 200:
            return GeneralImage(await response.read())

        elif response.status == 422:
            raise ValidationError("Recieved an invalid input")

        else:
            raise HTTPException(f"HTTP Error: {response.status}")

    @classmethod
    async def pills(cls, text: str) -> GeneralImage:
        """
        :class:`GeneralImage` Creates a pills meme image.
        """
        response = await HTTPClient().get(f"pills?text={text}")

        if response.status == 200:
            return GeneralImage(await response.read())

        elif response.status == 422:
            raise ValidationError("Recieved an invalid input")

        else:
            raise HTTPException(f"HTTP Error: {response.status}")

    @classmethod
    async def balloon(cls, text: str, person: str, stopper: str) -> GeneralImage:
        """
        :class:`GeneralImage` Creates a balloon meme image.
        """
        response = await HTTPClient().get(f"balloon?text={text}&person={person}&stopper={stopper}")

        if response.status == 200:
            return GeneralImage(await response.read())

        elif response.status == 422:
            raise ValidationError("Recieved an invalid input")

        else:
            raise HTTPException(f"HTTP Error: {response.status}")

    @classmethod
    async def waifu(cls) -> GeneralImage:
        """
        :class:`GeneralImage` Gets a waifu image.
        """
        response = await HTTPClient().get("waifu")

        if response.status == 200:
            return GeneralImage(await response.read())

        elif response.status == 422:
            raise ValidationError("Recieved an invalid input")

        else:
            raise HTTPException(f"HTTP Error: {response.status}")

    @classmethod
    async def qrcode(cls, query: str, drawer: Optional[int] = 1, mask: Optional[int] = 1) -> GeneralImage:
        """
        :class:`GeneralImage` Gets a qrcode image.
        """
        response = await HTTPClient().get(f"qrcode?query={query}&drawer={drawer}&mask={mask}")

        if response.status == 200:
            return GeneralImage(await response.read())

        elif response.status == 422:
            raise ValidationError("Recieved an invalid input")

        else:
            raise HTTPException(f"HTTP Error: {response.status}")
