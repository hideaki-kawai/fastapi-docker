from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

from sqlalchemy.orm import sessionmaker, declarative_base

# DB接続情報
ASYNC_DB_URL = "mysql+aiomysql://root@db:3306/demo?charset=utf8"

# DB接続を管理するためのエンジンオブジェクト
async_db_engine = create_async_engine(ASYNC_DB_URL, echo=True)

async_db_session = sessionmaker(
    autocommit=False, autoflush=False, bind=async_db_engine, class_=AsyncSession)

Base = declarative_base()


async def get_db():
    async with async_db_session() as session:
        yield session
