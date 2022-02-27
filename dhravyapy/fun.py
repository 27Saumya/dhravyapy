from .http import HTTPClient
from typing import *
from .errors import *
from .assets import Meme, TruthOrDare


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

    async def single_meme(self) -> str:
        """
        :class:`str`: Gets a single meme from the API.

        Note::
            This just returns the URL of the endpoint.
            Reason::
                There is no json in this response.
                There is direct the image of the meme.
                If you want a meme with all properties, use :meth:`meme`.
        """
        return await HTTPClient().get("meme")

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
