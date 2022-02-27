from typing import *
from .http import HTTPClient
import aiofiles
from .errors import HTTPException

class Meme:
    """
    The class to get meme related data from the API
    """
    
    def __init__(self, json: dict):
        self.json = json

    async def save(self, path: str) -> None:
        """
        Saves the meme as an image.

        Parameters
        ----------
        path : Filename and the Path to save the image :class:`str`

        Example
        -------
        >>> meme = await dhravyapy.Fun().meme("random")
        >>> await meme.save(f"meme.{meme.file_extension}")
        """
        r = await HTTPClient()._get(self.url)
        if r.status == 200:
            f = await aiofiles.open(path, "wb")
            await f.write(await r.read())
            await f.close()
        else:
            raise HTTPException(f"HTTP Error: {r.status}")
    
    @property
    def url(self) -> str:
        """
        :class:`str`: The URL of the meme.
        """
        return self.json["data"]["url"]
    
    @property
    def id(self) -> str:
        """
        :class:`str`: The ID of the meme.
        """
        return self.json["data"]["id"]
    
    @property
    def subreddit(self) -> str:
        """
        :class:`str`: The subreddit of the meme.
        """
        return self.json["data"]["subreddit"]
    
    @property
    def title(self) -> str:
        """
        :class:`str`: The title of the meme.
        """
        return self.json["data"]["title"]
    
    @property
    def score(self) -> int:
        """
        :class:`int`: The score of the meme.
        """
        return self.json["data"]["score"]
    
    @property
    def selftext(self) -> str:
        """
        :class:`str`: The selftext of the meme.
        """
        return self.json["data"]["selftext"]
    
    @property
    def is_nsfw(self) -> bool:
        """
        :class:`bool`: Whether the meme is NSFW.
        """
        return self.json["data"]["is_nsfw"]
    
    @property
    def dict(self) -> dict:
        """
        :class:`dict`: The meme's json in a dictionary.
        """
        return self.json["data"]
    
    @property
    def file_extension(self) -> str:
        """
        :class:`str`: The file extension of the meme.
        """
        return self.url.split(".")[-1]