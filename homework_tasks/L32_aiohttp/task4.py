"""
(Proste) Aiohttp - Proste API JSON: Stwórz handler na ścieżce /api/status , który
metodą GET zwróci odpowiedź JSON: {"status": "OK", "server_time": "..."} (użyj
datetime.now() do czasu i web.json_response ).
"""

from aiohttp import web
from datetime import datetime


async def handle_status(request: web.Request):
    return web.json_response({"status": "OK", "server_time": str(datetime.now())})


app = web.Application()
app.add_routes([web.get('/api/status', handle_status)])

if __name__ == "__main__":
    web.run_app(app , host='127.0.0.1', port=8081)
