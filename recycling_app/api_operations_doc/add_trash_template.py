import asyncio
import aiohttp
from endpoints import ApiUrls


class ConnectionHandler:
    @staticmethod
    async def post():
        async with aiohttp.ClientSession() as session:
            async with session.get(ApiUrls.TRASHES_URL) as resp:
                trashes = await resp.json()
                print(trashes)


asyncio.run(ConnectionHandler.post())
