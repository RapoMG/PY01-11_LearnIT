"""
Obsługa błędu: W handlerze z zadania 3 ( /witaj/{imie} ), dodaj
sprawdzenie. Jeśli imie to "admin", podnieś wyjątek raise
web.HTTPForbidden(text="Dostęp dla admina zabroniony") .
"""

from aiohttp import web

async def handle_index(request):
    return web.Response(text="<h1>Witaj na mojej stronie!</h1>", content_type='text/html')

async def handle_hello(request):
    name = request.match_info.get("name", "Świecie")
    if name == "admin":
        raise web.HTTPForbidden(text="Dostęp dla admina zabroniony")
    
    return web.Response(text=f"Witaj, {name}!", content_type='text/html')


app = web.Application()
app.router.add_get('/', handle_index)
app.router.add_get('/witaj/{name}', handle_hello)

if __name__ == "__main__":
    web.run_app(app, host='127.0.0.1', port=8081)