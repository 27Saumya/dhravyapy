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
from .assets import Trivia, SongInfo


class Info:
    """
    The class to get information related data from the API
    """

    @classmethod
    async def fact(cls, simple: Optional[bool] = False) -> str:
        """
        :class:`str`: Gets a random fact.

        Parameters
        ----------
        simple : Wheter the fact should be simple. Optional[:class:`bool`]
        """
        response = await HTTPClient().get(f"fact?simple={simple}")

        if response.status == 200:
            json = await response.json()
            return json["data"]["Fact"]

        elif response.status == 422:
            raise ValidationError("Recieved an invalid input")

        else:
            raise HTTPException(f"HTTP Error: {response.status}")

    @classmethod
    async def trivia(cls, simple: Optional[bool] = False) -> Trivia:
        """
        :class:`str`: Gets a random trivia question.

        Parameters
        ----------
        simple : Wheter the trivia question should be simple. Optional[:class:`bool`]
        """
        response = await HTTPClient().get(f"trivia?simple={simple}")

        if response.status == 200:
            json = await response.json()
            return Trivia(json)

        elif response.status == 422:
            raise ValidationError("Recieved an invalid input")

        else:
            raise HTTPException(f"HTTP Error: {response.status}")

    @classmethod
    async def lyrics(cls, song: str, simple: Optional[bool] = False) -> str:
        """
        :class:`str`: Gets the lyrics of a song.

        Parameters
        ----------
        song : The name of the song. :class:`str`
        simple : Wheter the lyrics should be simple. Optional[:class:`bool`]
        """
        response = await HTTPClient().get(f"lyrics?song={song}&simple={simple}")

        if response.status == 200:
            json = await response.json()
            return json["data"]["lyrics"]

        elif response.status == 422:
            raise ValidationError("Recieved an invalid input")

        else:
            raise HTTPException(f"HTTP Error: {response.status}")

    @classmethod
    async def song_info(cls, song: str) -> SongInfo:
        """
        :class:`str`: Gets the information of a song.

        Parameters
        ----------
        song : The name of the song. :class:`str`
        """
        response = await HTTPClient().get(f"songinfo?song={song}")

        if response.status == 200:
            json = await response.json()
            return SongInfo(json)

        elif response.status == 422:
            raise ValidationError("Recieved an invalid input")

        else:
            raise HTTPException(f"HTTP Error: {response.status}")

    @classmethod
    async def minecraft_status(cls, host: str, port: Optional[str] = None) -> str:
        """
        :class:`str`: Gets the status of a minecraft server.

        Parameters
        ----------
        host : The hostname of the server. Required[:class:`str`]
        port : The port of the server. Optional[:class:`str`]
        """
        response = await HTTPClient().get(f"mcstatus?host={host}&port={port}")

        if response.status == 200:
            json = await response.json()
            return json  # Don't know what it returns

        elif response.status == 422:
            raise ValidationError("Recieved an invalid input")

        else:
            raise HTTPException(f"HTTP Error: {response.status}")

    @classmethod
    async def bored(cls) -> str:
        """
        :class:`str`: Gets a bored fact.
        """
        response = await HTTPClient().get("bored")

        if response.status == 200:
            json = await response.json()
            return json["data"]["activity"]

        else:
            raise HTTPException(f"HTTP Error: {response.status}")

    @classmethod
    async def numberfact(cls, number: int) -> str:
        """
        :class:`str`: Gets a fact about a number.

        Parameters
        ----------
        number : The number to get a fact about. :class:`int`
        """
        response = await HTTPClient().get(f"numberfact?number={number}")

        if response.status == 200:
            json = await response.json()
            return json["data"]

        elif response.status == 422:
            raise ValidationError("Recieved an invalid input")

        else:
            raise HTTPException(f"HTTP Error: {response.status}")
