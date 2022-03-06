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
from .assets import RandomUserInfo


class Misc:
    """
    The class to get Miscellaneous data from the API
    """

    async def compliment(self, simple: Optional[bool] = False) -> str:
        """
        :class:`str`: Gets a random compliment.

        Parameters
        ----------
        simple : Wheter the compliment should be simple. Optional[:class:`bool`]
        """
        response = await HTTPClient().get(f"compliment?simple={simple}")

        if response.status == 200:
            json = await response.json()
            return json["data"]["Compliment"]

        elif response.status == 422:
            raise ValidationError("Recieved an invalid input")

        else:
            raise HTTPException(f"HTTP Error: {response.status}")

    async def topic(self, simple: Optional[bool] = False) -> str:
        """
        :class:`str`: Gets a random topic.

        Parameters
        ----------
        simple : Wheter the topic should be simple. Optional[:class:`bool`]
        """
        response = await HTTPClient().get(f"topic?simple={simple}")

        if response.status == 200:
            json = await response.json()
            return json["data"]["Topic"]

        elif response.status == 422:
            raise ValidationError("Recieved an invalid input")

        else:
            raise HTTPException(f"HTTP Error: {response.status}")

    async def translate(
        self,
        text: str,
        from_lang: str,
        to_lang: Optional[str] = "en",
        simple: Optional[bool] = False,
    ) -> str:
        """
        :class:`str`: Translates text from one language to another.

        Parameters
        ----------
        text : The text to translate. :class:`str`
        from_lang : The language to translate from. :class:`str`
        to_lang : The language to translate to. Optional[:class:`str`]
        simple : Wheter the translation should be simple. Optional[:class:`bool`]
        """
        response = await HTTPClient().get(
            f"translate?text={text}&from={from_lang}&to={to_lang}&simple={simple}"
        )

        if response.status == 200:
            json = await response.json()
            return json["data"]  # Don't know what it returns.. so returned dict for now

        elif response.status == 422:
            raise ValidationError("Recieved an invalid input")

        else:
            raise HTTPException(f"HTTP Error: {response.status}")

    async def ascii(self, text: str, font: Optional[str] = None):
        """
        :class:`str`: Gets an ASCII art of the text.

        Parameters
        ----------
        text : The text to get an ASCII art of. :class:`str`
        font : The font to use. Optional[:class:`str`]
        """
        response = await HTTPClient().get(f"ascii?text={text}&font={font}")

        if response.status == 200:
            json = await response.json()
            return json["data"]

        elif response.status == 422:
            raise ValidationError("Recieved an invalid input")

        else:
            raise HTTPException(f"HTTP Error: {response.status}")

    async def randomuser(self) -> RandomUserInfo:
        """
        :class:`RandomUserInfo`: Gets a random user.
        """
        response = await HTTPClient().get("randomuser")

        if response.status == 200:
            json = await response.json()
            return RandomUserInfo(json)

        else:
            raise HTTPException(f"HTTP Error: {response.status}")

    async def autofill(self, query: str) -> List[str]:
        """
        :class:`List[str]`: Gets autofill suggestions for the query.

        Parameters
        ----------
        query : The query to get autofill suggestions for. :class:`str`
        """
        response = await HTTPClient().get(f"autofill?query={query}")

        if response.status == 200:
            json = await response.json()
            return json["data"]

        elif response.status == 422:
            raise ValidationError("Recieved an invalid input")

        else:
            raise HTTPException(f"HTTP Error: {response.status}")
