"""
Aiohttp Klient - Gather: Rozbuduj zadanie 12. Napisz korutynę
fetch(session, url) , która pobiera dane. W main stwórz listę 3 różnych URL-i (np. z
https://api.publicapis.org/random?auth=null - wywołaj 3 razy) i użyj
asyncio.gather , aby pobrać je wszystkie jednocześnie.
"""

import asyncio
import aiohttp
import requests

async def fetch(session, url):
    async with session.get(url) as response:
        try:
            response.raise_for_status()
            return await response.json()
        except requests.exceptions.HTTPError as e:
            print("HTTP error occurred:", e)
        except requests.exceptions.RequestException as e:
            print("A request error occurred:", e)
        except Exception as exc:
            print('Request failed', exc)
        


async def main():
    urls = [
        #'https://pokeapi.co/api/v2/pokemon/pikachu',
        "https://pokeapi.co/api/v2/evolution-chain/1",
        'https://fakerapi.it/api/v1/addresses?_quantity=1',
        'https://official-joke-api.appspot.com/jokes/random'
    ]
    async with aiohttp.ClientSession() as session:
        results = await asyncio.gather(*[fetch(session, url) for url in urls])
        for result in results:
            print('====='*5)
        
            print(type(result))
            for k, v in result.items():
                if type(v) == dict:
                    print(f"{k}:")
                    for k2, v2 in v.items():
                        print(f"\t{k2}: {v2}")
                    continue
                print(f"{k}: {v}\n")
        print('====='*5)


if __name__ == '__main__':
    asyncio.run(main())