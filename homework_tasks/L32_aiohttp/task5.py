"""
Aiohttp - Odczyt query params: Stwórz handler /api/search , który odczyta
z request.query parametr q . Jeśli parametr istnieje, zwróć JSON {"szukana_fraza":
"wartosc_q"} . Jeśli nie, zwróć {"błąd": "Brak parametru q"} .
"""

from aiohttp import web


async def handle_search(request):
    #query = request.query
    q = request.query.get('q')
    if q:
        return web.json_response({"szukana_fraza": q})
    else:
        return web.json_response({"błąd": "Brak parametru q"}, status=400) # 400 - bad request
        
    

app = web.Application()
app.router.add_get('/api/search', handle_search)
if  __name__ == "__main__": 
    web.run_app(app , host='127.0.0.1', port=8081)