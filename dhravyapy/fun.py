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
from .assets import Meme, TruthOrDare, GeneralImage


class Fun:
    """
    The class to get fun related data from the API
    """

    async def eightball(self, *, simple: Optional[bool] = False) -> str:
        """
        :class:`str`: Gets a random 8ball response.

        Parameters
        ----------
        simple : Wheter the response should be simple. Optional[:class:`bool`]
        """
        response = await HTTPClient().get(f"fun/8ball?simple={simple}")

        if response.status == 200:
            json = await response.json()
            return json["data"]["answer"]

        else:
            raise HTTPException(f"HTTP Error: {response.status}")

    async def meme(self, topic: str) -> Meme:
        """
        :class:`Meme`: Gets a meme from the API.

        Parameters
        ----------
        topic : :class:`str`
        """
        response = await HTTPClient().get(f"meme/{topic}")

        if response.status == 200:
            json = await response.json()
            return Meme(json)

        elif response.status == 422:
            raise ValidationError("Recieved an invalid input")

        elif response.status == 500:
            raise HTTPException("Internal Server Error")

        else:
            raise HTTPException(f"HTTP Error: {response.status}")

    async def single_meme(self) -> GeneralImage:
        """
        :class:`GeneralImage`: Gets a single meme from the API.

        Note::
            This just returns the :class:`GeneralImage` class.
            You can only use `.save()` in this method.
            Reason::
                There is no json in this response.
                There is direct the image of the meme.
                If you want a meme with all properties, use :meth:`meme`.
        """
        response = await HTTPClient().get("meme")

        if response.status == 200:
            return GeneralImage(await response.read())

        else:
            raise HTTPException(f"HTTP Error: {response.status}")

    async def wyr(self, simple: Optional[bool] = False) -> List[str]:
        """
        :class:`str`: Gets a random "Would You Rather" question.

        Parameters
        ----------
        simple : Wheter the question should be simple. Optional[:class:`bool`]
        """
        response = await HTTPClient().get(f"wyr?simple={simple}")

        if response.status == 200:
            json = await response.json()
            return json["data"]["Would You Rather"]

        elif response.status == 422:
            raise ValidationError("Recieved an invalid input")

        else:
            raise HTTPException(f"HTTP Error: {response.status}")

    async def truthordare(self, simple: Optional[bool] = False) -> TruthOrDare:
        """
        :class:`str`: Gets a random truth or dare.

        Parameters
        ----------
        simple : Wheter the question should be simple. Optional[:class:`bool`]
        """
        response = await HTTPClient().get(f"truthordare?simple={simple}")

        if response.status == 200:
            json = await response.json()
            return TruthOrDare(json)

        elif response.status == 422:
            raise ValidationError("Recieved an invalid input")

        else:
            raise HTTPException(f"HTTP Error: {response.status}")

    async def roast(self, simple: Optional[bool] = False) -> str:
        """
        :class:`str`: Gets a random roast.

        Parameters
        ----------
        simple : Wheter the roast should be simple. Optional[:class:`bool`]
        """
        response = await HTTPClient().get(f"roast?simple={simple}")

        if response.status == 200:
            json = await response.json()
            return json["data"]["Roast"]

        elif response.status == 422:
            raise ValidationError("Recieved an invalid input")

        else:
            raise HTTPException(f"HTTP Error: {response.status}")

    async def truth(self, simple: Optional[bool] = False) -> str:
        """
        :class:`str`: Gets a random truth.

        Parameters
        ----------
        simple : Wheter the truth should be simple. Optional[:class:`bool`]

        Note::
        ------
            This is a shortcut for :meth:`Fun().truthordare().truth`.
        """
        response = await HTTPClient().get(f"truth?simple={simple}")

        if response.status == 200:
            json = await response.json()
            return json["data"]["Truth"]

        elif response.status == 422:
            raise ValidationError("Recieved an invalid input")

        else:
            raise HTTPException(f"HTTP Error: {response.status}")

    async def dare(self, simple: Optional[bool] = False) -> str:
        """
        :class:`str`: Gets a random dare.

        Parameters
        ----------
        simple : Wheter the dare should be simple. Optional[:class:`bool`]

        Note::
        ------
            This is a shortcut for :meth:`Fun().truthordare().dare`.
        """
        response = await HTTPClient().get(f"dare?simple={simple}")

        if response.status == 200:
            json = await response.json()
            return json["data"]["Dare"]

        elif response.status == 422:
            raise ValidationError("Recieved an invalid input")

        else:
            raise HTTPException(f"HTTP Error: {response.status}")

    async def joke(self, simple: Optional[bool] = False) -> str:
        """
        :class:`str`: Gets a random joke.

        Parameters
        ----------
        simple : Wheter the joke should be simple. Optional[:class:`bool`]
        """
        response = await HTTPClient().get(f"joke?simple={simple}")

        if response.status == 200:
            json = await response.json()
            return json["data"]["Joke"]

        elif response.status == 422:
            raise ValidationError("Recieved an invalid input")

        else:
            raise HTTPException(f"HTTP Error: {response.status}")

    async def neverhaveiever(self, simple: Optional[bool] = False) -> str:
        """
        :class:`str`: Gets a random "Never Have I Ever" question.

        Parameters
        ----------
        simple : Wheter the question should be simple. Optional[:class:`bool`]
        """
        response = await HTTPClient().get(f"neverhaveiever?simple={simple}")

        if response.status == 200:
            json = await response.json()
            return json["data"]["Topic"]

        elif response.status == 422:
            raise ValidationError("Recieved an invalid input")

        else:
            raise HTTPException(f"HTTP Error: {response.status}")
