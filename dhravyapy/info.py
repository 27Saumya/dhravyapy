from .http import HTTPClient
from typing import *
from .errors import *
from .assets import Trivia, SongInfo


class Info:
    """
    The class to get information related data from the API
    """

    async def fact(self, simple: Optional[bool] = False) -> str:
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

    async def trivia(self, simple: Optional[bool] = False) -> Trivia:
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

    async def lyrics(self, song: str, simple: Optional[bool] = False) -> str:
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

    async def song_info(self, song: str) -> SongInfo:
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

    async def minecraft_status(self, host: str, port: Optional[str] = None) -> str:
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

    async def bored(self) -> str:
        """
        :class:`str`: Gets a bored fact.
        """
        response = await HTTPClient().get("bored")

        if response.status == 200:
            json = await response.json()
            return json["data"]["activity"]

        else:
            raise HTTPException(f"HTTP Error: {response.status}")

    async def numberfact(self, number: int) -> str:
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
