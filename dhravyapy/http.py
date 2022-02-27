import aiohttp


class HTTPClient(aiohttp.ClientSession):
    BASE_URL = "https://api.dhravya.me/"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def get(self, url: str) -> aiohttp.ClientResponse:
        return await super().get(self.BASE_URL + url)
    
    async def _get(self, url: str) -> aiohttp.ClientResponse:
        return await super().get(url)