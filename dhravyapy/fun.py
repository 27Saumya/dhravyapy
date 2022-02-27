from .http import HTTPClient
from typing import *
from .errors import *
from .meme import Meme

class Fun:
    """
    The class to get fun related data from the API
    """
    async def eightball(self, *, simple: Optional[bool] = False) -> str:
        """
        :class:`str`: Gets a random 8ball response.

        Parameters
        ----------
        simple : Optional[:class:`bool`]
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