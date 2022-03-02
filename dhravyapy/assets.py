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
            
    aysnc def bytes(self):
        r = await HTTPClient()._get(self.url)
        if r.status == 200:
            bytes = await r.read()
            return bytes
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


class TruthOrDare:
    """
    The class to return the data from the "truthordare" endpoint.
    """

    def __init__(self, json: dict):
        self.json = json

    @property
    def truth(self) -> str:
        """
        :class:`str`: The truth.
        """
        return self.json["data"]["Truth"]

    @property
    def dare(self) -> str:
        """
        :class:`str`: The dare.
        """
        return self.json["data"]["Dare"]


class Trivia:
    """
    The class to return the data from the "trivia" endpoint.
    """

    def __init__(self, json: dict):
        self.json = json

    @property
    def question(self) -> str:
        """
        :class:`str`: The question.
        """
        return self.json["data"]["Question"]

    @property
    def answer(self) -> str:
        """
        :class:`str`: The answer.
        """
        return self.json["data"]["Answer"]


class SongInfo:
    """
    The class to return the data from the "songinfo" endpoint.
    """

    def __init__(self, json: dict):
        self.json = json

    @property
    def title(self) -> str:
        """
        :class:`str`: The title of the song.
        """
        return self.json["response"]["result"]["full_title"]

    @property
    def artist(self) -> str:
        """
        :class:`str`: The artist of the song.
        """
        return self.json["response"]["result"]["artist_names"]

    @property
    def thumnail_image_url(self) -> str:
        """
        :class:`str`: The thumbnail image url of the song.
        """
        return self.json["response"]["result"]["header_image_thumbnail_url"]

    @property
    def image_url(self) -> str:
        """
        :class:`str`: The image url of the song.
        """
        return self.json["response"]["result"]["header_image_url"]

    async def lyrics(self) -> str:
        """
        :class:`str`: The lyrics of the song.
        """
        await Info().lyrics(self.json["response"]["result"]["full_title"])

    @property
    def dict(self) -> dict:
        """
        :class:`dict`: The song's json in a dictionary.
        """
        return self.json["response"]


class BoredInfo:
    """
    The class to return the data from the "bored" endpoint.
    """

    def __init__(self, json: dict):
        self.json = json

    @property
    def activity(self) -> str:
        """
        :class:`str`: The activity.
        """
        return self.json["data"]["activity"]

    @property
    def type(self) -> str:
        """
        :class:`str`: The type of the activity.
        """
        return self.json["data"]["type"]

    @property
    def participants(self) -> int:
        """
        :class:`str`: The participants of the activity.
        """
        return self.json["data"]["participants"]

    @property
    def price(self) -> int:
        """
        :class:`str`: The price of the activity.
        """
        return self.json["data"]["price"]

    @property
    def link(self) -> str:
        """
        :class:`str`: The link of the activity.
        """
        return self.json["data"]["link"]

    @property
    def accessibility(self) -> Union[float, int]:
        """
        :class:`str`: The accessibility of the activity.
        """
        return self.json["data"]["access"]

    @property
    def dict(self) -> dict:
        """
        :class:`dict`: The activity's json in a dictionary.
        """
        return self.json["data"]


class RandomUserInfo:
    """
    The class to return the data from the "randomuser" endpoint.
    """

    def __init__(self, json: dict):
        self.json = json

    @property
    def name(self) -> str:
        """
        :class:`str`: The name of the user.
        """
        return self.json["data"]["name"]["first"]

    @property
    def lastname(self) -> str:
        """
        :class:`str`: The lastname of the user.
        """
        return self.json["data"]["name"]["last"]

    @property
    def full_name(self) -> str:
        """
        :class:`str`: The full name of the user.
        """
        return (
            self.json["data"]["name"]["first"] + " " + self.json["data"]["name"]["last"]
        )

    @property
    def email(self) -> str:
        """
        :class:`str`: The email of the user.
        """
        return self.json["data"]["email"]

    @property
    def gender(self) -> str:
        """
        :class:`str`: The gender of the user.
        """
        return self.json["data"]["gender"]

    @property
    def location(self) -> Dict[str, Union[int, str]]:
        """
        Dict[Union[:class:`int`, :class:`str`]]`: The location of the user in a dictionary
        """
        return self.json["location"]

    @property
    def timezone_offset(self) -> str:
        """
        :class:`str`: The timezone offset of the user.
        """
        return self.json["data"]["location"]["timezone"]["offset"]

    @property
    def timezone_region(self) -> str:
        """
        :class:`str`: The timezone region of the user.
        """
        return self.json["data"]["location"]["timezone"]["description"]

    @property
    def login(self) -> Dict[str, Union[str, int]]:
        """
        Dict[:class:`str`] The login of the user in a dictionary
        """
        return self.json["data"]["login"]

    @property
    def dob(self) -> str:
        """
        :class:`str`: The date of birth of the user.
        """
        return self.json["data"]["dob"]["date"]

    @property
    def age(self) -> int:
        """
        :class:`int`: The age of the user.
        """
        return self.json["data"]["dob"]["age"]

    @property
    def registered(self) -> str:
        """
        :class:`str`: The registered date of the user.
        """
        return self.json["data"]["registered"]["date"]

    @property
    def phone(self) -> str:
        """
        :class:`str`: The phone number of the user.
        """
        return self.json["data"]["phone"]

    @property
    def cell(self) -> str:
        """
        :class:`str`: The cell phone number of the user.
        """
        return self.json["data"]["cell"]

    @property
    def id(self) -> Dict[str, Union[int, str]]:
        """
        Dict[:class:`str`]: The id of the user.
        """
        return self.json["data"]["id"]["value"]

    @property
    def large_picture(self) -> str:
        """
        :class:`str`: The large picture of the user.
        """
        return self.json["data"]["picture"]["large"]

    @property
    def medium_picture(self) -> str:
        """
        :class:`str`: The medium picture of the user.
        """
        return self.json["data"]["picture"]["medium"]

    @property
    def thumbnail(self) -> str:
        """
        :class:`str`: The thumbnail picture of the user.
        """
        return self.json["data"]["picture"]["thumbnail"]

    @property
    def dict(self) -> dict:
        """
        :class:`dict`: The user's json in a dictionary.
        """
        return self.json["data"]


class Animal:
    """
    The class to return the data from the "animal" endpoint.
    """

    def __init__(self, _bytes: Union[bytes, str]):
        self.bytes = _bytes

    async def save(self, path: str) -> None:
        """
        Save the image of the animal.

        Parameters
        ----------
        path : Filename and the Path to save the image :class:`str`

        Example
        -------
        >>> dog = await dhravyapy.Animal().dog()
        >>> await dog.save("dog.png")
        """
        f = await aiofiles.open(path, "wb")
        await f.write(self.bytes)
        await f.close()


class GeneralImage:
    """
    The class to return the data from images in general endpoints.
    """

    def __init__(self, _bytes: Union[bytes, str]):
        self.bytes = _bytes

    async def save(self, path: str) -> None:
        """
        Save the image.

        Parameters
        ----------
        path : Filename and the Path to save the image :class:`str`

        Example
        -------
        >>> waifu = await dhravyapy.Image().waifu()
        >>> await waifu.save("waifu.png")
        """
        f = await aiofiles.open(path, "wb")
        await f.write(self.bytes)
        await f.close()
