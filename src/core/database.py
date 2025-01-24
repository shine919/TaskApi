from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession
from src.core.config import settings

engine = create_async_engine(
    url=settings.DATABASE_URL,
    echo=True,
    pool_size=5,
    max_overflow=100,
)  # создаем асинхронный движок и говорим ему куда подключатся и с какими параметрами
# echo=True когда хотим видеть логи ,pool_size - количество открытых подключений ,max_overflow - если открытых не хватает

session_factory = async_sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
)


async def get_session() -> AsyncSession:
    async with session_factory() as session:
        yield session
