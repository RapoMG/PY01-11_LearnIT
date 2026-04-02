"""
Aiohttp - Mock API dla AI: Stwórz handler POST na /api/v1/chat .
Handler ma:
1. Oczekiwać JSON-a: {"prompt": "jakaś treść"} .
2. Symulować długie przetwarzanie przez AI: await asyncio.sleep(3) .
3. Zwrócić odpowiedź JSON: {"response": f"Otrzymałem twój prompt: '{prompt_text}' i
przetworzyłem go."}.
(To ćwiczenie pokazuje, jak serwer aiohttp radzi sobie z długimi zadaniami I/O, nie
blokując innych zapytań).
"""

import asyncio
from aiohttp import web

app = web.Application()


async def handler(request):
    data = await request.json()
    try:
        prompt_text = data['prompt']
    except KeyError:
        return web.json_response({'error': 'Missing prompt'}, status=400)
    

    await asyncio.sleep(5)
    return web.json_response({'response': f"Otrzymałem twój prompt: '{prompt_text}' i przetworzyłem go."})


if __name__ == "__main__":
    app.router.add_post('/api/v1/chat', handler)
    web.run_app(app , host='127.0.0.1', port=8081)