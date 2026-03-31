"""
Task 9:
    CRUD API - Produkty (POST): Używając aplikacji z przykładu (z gotową
    integracją SQLAlchemy ):
    1. Dodaj model Product (z zadania 7) do pliku.
    2. Pamiętaj o dodaniu go do Base.metadata.create_all .
    3. Stwórz handler POST na /products , który odczyta name i price z JSON, stworzy
    nowy obiekt Product i zapisze go w bazie.
    4. Handler powinien zwrócić dane nowego produktu (wraz z ID) i status 201

Task 10:
    CRUD API - Produkty (GET Lista): Bazując na zadaniu 9, stwórz handler
    GET na /products , который pobierze wszystkie produkty z bazy danych ( select(Product) )
    i zwróci je jako listę obiektów JSON

Task 11:
    CRUD API - Produkty (GET Pojedynczy): Bazując na zadaniu 10, stwórz
    handler GET na /products/{id} . Handler ma pobrać ID z match_info , znaleźć produkt
    w bazie ( select(Product).where(Product.id == product_id) ). Jeśli produkt istnieje,
    zwróć jego dane JSON. Jeśli nie, podnieś wyjątek web.HTTPNotFound() .

Task 14:
    CRUD API - Produkty (PUT/PATCH): Bazując na zadaniu 11, stwórz
    handler PUT (lub PATCH ) na /products/{id} . Handler ma:
    1. Pobrać produkt (i zwrócić 404, jeśli go nie ma).
    2. Odczytać nowe dane name i/lub price z await request.json() .
    3. Zaktualizują atrybuty obiektu produktu.
    4. Zapisać zmiany w bazie (w ramach sesji i transakcji).
    5. Zwrócić zaktualizowane dane produktu.

Task 15:
    CRUD API - Produkty (DELETE): Bazując na zadaniu 11, stwórz handler
    DELETE na /products/{id} . Handler ma pobrać obiekt, usunąć go ( await
    session.delete(product) ) i zwrócić pustą odpowiedź ze statusem 204 (No Content)

Task 20:
    SQLAlchemy Async - JOIN: (Znacie JOIN). Dodaj do modelu Product
    relację ForeignKey do User (twórca produktu). Zmodyfikuj handler GET
    /products/{id} , aby pobierał produkt wraz z nazwą użytkownika,ęty go stworzył
    (używając select(Product, User).join(User) lub
    options(joinedload(Product.user)) - opcja dla ambitnych).
"""

import os
from aiohttp import web

# Importy specyficzne dla Async SQLAlchemy
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

# Importy modeli (znane z synchronicznego SQLAlchemy)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Integer, select

# --- Ustawienia Bazy Danych ---
# Upewnij się, że masz działającą bazę PostgreSQL!
# Używamy zmiennej środowiskowej lub domyślnej wartości.
# FORMAT: postgresql+ASYNC_DRIVER://user:password@host/dbname
DB_URL = os.environ.get("DB_URL", "postgresql+asyncpg://postgres:asdf@localhost/aio_test_db")

# --- Definicje Modeli (tak jak w synchronicznym SQLAlchemy 2.0) ---
class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "app_users" # 'users' to często słowo kluczowe w SQL
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    email: Mapped[str] = mapped_column(String(100))
    
    # Metoda pomocnicza do konwersji obiektu na słownik
    def to_dict(self):
        return {
        "id": self.id,
        "username": self.username,
        "email": self.email
        }
    
    
class Product(Base):
    __tablename__ = "products"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))  # This should be unique or field barcode should exist 
    price: Mapped[int] = mapped_column(Integer)

    def to_dict(self):
        return {"id": self.id, "name": self.name, "price": self.price}


    def __str__(self):
        return f"Product(id={self.id}, name={self.name}, price={self.price})"
    

# --- Kontekst Aplikacji (Startup/Cleanup) ---
async def init_db(app: web.Application):
    """Sygnał on_startup: tworzy silnik i sessionmaker."""
    print(f"Inicjalizuję połączenie z bazą danych: {DB_URL}")

    # 1. Tworzymy asynchroniczny silnik
    engine = create_async_engine(DB_URL, echo=True) # echo=True pokaże zapytania SQL

    # 2. Tworzymy fabrykę sesji (Session Maker)
    # W trybie async, sessionmaker tworzymy z `class_=AsyncSession`
    async_session_factory = async_sessionmaker(
        engine,
        expire_on_commit=False, # Ważne dla async
        class_=AsyncSession
    )

    # 3. (Opcjonalnie) Stworzenie tabel przy starcie (tylko dla deweloperki!)
    async with engine.begin() as conn:
        # Używamy run_sync do uruchomienia synchronicznej metody create_all
        await conn.run_sync(Base.metadata.create_all)

    # 4. Przechowujemy fabrykę sesji w obiekcie aplikacji
    app["db_session_factory"] = async_session_factory
    print("Połączenie z bazą danych gotowe.")

async def close_db(app: web.Application):
    """Sygnał on_cleanup: zamyka silnik."""

    # SQLAlchemy 2.0+ zaleca użycie `engine.dispose()` w kontekście async
    # Jeśli silnik jest przechowywany w `app`
    # W tym prostym przypadku, `web.run_app` często zarządza tym
    # pośrednio, ale jawne czyszczenie jest bezpieczniejsze.
    print("Zamykam pulę połączeń z bazą danych.")

    # Jeśli przechowywaliśmy engine w app:
    # if 'db_engine' in app:
    # await app['db_engine'].dispose()
    pass

# --- Handlery korzystające z Bazy Danych ---
async def create_user(request: web.Request):
    """Handler POST /users - tworzy nowego użytkownika."""
    try:
        data = await request.json()
        username = data["username"]
        email = data["email"]
    except Exception:
        raise web.HTTPBadRequest(text="Oczekiwano JSON z 'username' i 'email'")
    # Pobieramy fabrykę sesji z aplikacji
    session_factory: async_sessionmaker[AsyncSession] = request.app["db_session_factory"]
    
    # Otwieramy nową sesję
    # `async with` zarządza `await session.close()`
    async with session_factory() as session:
        # `async with session.begin()` zarządza `await session.commit()` lub `await session.rollback()`
        async with session.begin():
            # Sprawdzenie, czy użytkownik już istnieje
            stmt_exists = select(User).where(User.username == username)
            existing_user = await session.execute(stmt_exists)
            if existing_user.scalar_one_or_none() is not None:
                raise web.HTTPConflict(text=f"Użytkownik {username} już istnieje")
            
            # Tworzymy i dodajemy nowego użytkownika
            new_user = User(username=username, email=email)
            session.add(new_user)
            # Musimy `await session.flush()` aby dostać ID przed commitem
            await session.flush()
            user_data = new_user.to_dict()
    return web.json_response(user_data, status=201)

async def get_users(request: web.Request):
    """Handler GET /users - pobiera listę wszystkich użytkowników."""
    session_factory: async_sessionmaker[AsyncSession] = request.app["db_session_factory"]
    async with session_factory() as session:
        # Tworzymy zapytanie (identycznie jak w sync SQLAlchemy 2.0)
        stmt = select(User)
        # Wykonujemy zapytanie z `await`
        result = await session.execute(stmt)
        # Pobieramy obiekty
        # .scalars() pobiera pierwszą kolumnę (nasze obiekty User)
        # .all() materializuje listę (również operacja I/O)
        users = result.scalars().all()
        # Konwertujemy obiekty ORM na listę słowników
        users_data = [u.to_dict() for u in users]
        return web.json_response(users_data)

#### Task 9 ####
async def create_product(request: web.Request):
    """Handler POST /products - creates new product."""
    try:
        data = await request.json()
        name = data["name"]
        price = data["price"]
    except Exception:
        raise web.HTTPBadRequest(text="Oczekiwano JSON z 'name' i 'price'")
    # get factory from app
    session_factory: async_sessionmaker[AsyncSession] = request.app["db_session_factory"]

    #New session
    async with session_factory() as session:
        async with session.begin():
           
            new_product = Product(name=name, price=price)
            session.add(new_product)

            await session.flush()  # send everything to DB
            product_data = new_product.to_dict()

    return web.json_response(product_data, status=201)

#### Task 10 ####
async def get_products(request: web.Request):
    """Handler GET /products - get list of all products."""
    session_factory: async_sessionmaker[AsyncSession] = request.app["db_session_factory"]
    async with session_factory() as session:
        stmt = select(Product)
        result = await session.execute(stmt)
        products = result.scalars().all()
        products_data = [p.to_dict() for p in products]
        return web.json_response(products_data)

#### Task 11 ####
async def get_product(request: web.Request):
    """Handler GET /products/{product_id} - get product by id."""
    product_id = request.match_info["product_id"]
    session_factory: async_sessionmaker[AsyncSession] = request.app["db_session_factory"]
    async with session_factory() as session:
        stmt = select(Product).where(Product.id == product_id)
        result = await session.execute(stmt)
        product = result.scalar_one_or_none()
        if product is None:
            raise web.HTTPNotFound(text=f"Produkt o id {product_id} nie istnieje")
        return web.json_response(product.to_dict())

# --- Tworzenie Aplikacji ---
def create_app():
    app = web.Application()
    app.router.add_post("/users", create_user)
    app.router.add_get("/users", get_users)

    app.router.add_post("/products", create_product)  # task 9
    app.router.add_get("/products", get_products)  # task 10
    app.router.add_get("/products/{product_id}", get_product)  # task 11

    # Rejestrujemy sygnały
    app.on_startup.append(init_db)
    app.on_cleanup.append(close_db)
    return app

if __name__ == "__main__":
    app = create_app()
    print(f"--- Start serwera na [http://127.0.0.1:8081] (http://127.0.0.1:8081) ---")
    print(f"--- Upewnij się, że baza danych na {DB_URL} działa i jest utworzona. ---")
    web.run_app(app, port=8081)