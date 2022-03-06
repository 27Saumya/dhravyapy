"""
DhravyaAPI Wrapper
~~~~~~~~~~~~~~~~~~

A basic asynchronous wrapper for the [DhravyaAPI](https://api.dhravya.me).
"""

__title__ = "dhravyapy"
__author__ = "27Saumya"
__license__ = "MIT"
__version__ = "0.0.8"

from .fun import *
from .image import *
from .info import *
from .misc import *
from typing import Dict, Union


async def stats() -> Dict[str, Union[str, int]]:
    """
    :class:`dict`: Gets the stats of the API.
    """
    response = await HTTPClient().get("stats")

    if response.status == 200:
        json = await response.json()
        return json["data"]

    elif response.status == 422:
        raise ValidationError("Recieved an invalid input")

    else:
        raise HTTPException(f"HTTP Error: {response.status}")
