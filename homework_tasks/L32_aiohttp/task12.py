"""
Aiohttp Klient - Publiczne API: Aiohttp to także klient! Napisz osobny
skrypt .py (nie serwer), który w korutynie main :
1. Stworzy aiohttp.ClientSession() .
2. Wykona zapytanie GET na publiczne API:
https://api.coindesk.com/v1/bpi/currentprice.json .
3. Pobierze odpowiedź JSON ( await response.json() ).
4. Wypisze w konsoli cenę Bitcoina w USD.
Hint: Użyj async with aiohttp.ClientSession() as session: async with session.get(url) as response:


https://data-api.coindesk.com - current enterprise API
https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd - public API
"""

import asyncio
import aiohttp

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd') as response:
            data = await response.json()
            print(f"Bitcoin price: {data['bitcoin']['usd']} USD")


if __name__ == '__main__':
    asyncio.run(main())